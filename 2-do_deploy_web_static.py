#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers  """
from fabric.api import local, put, run, env
from os import path
from datetime import datetime

env.hosts = ["{}@34.139.180.201".format(env.user),
             "{}@54.86.32.22".format(env.user)]


def do_pack():
    """ Method do_pack """
    if not path.exists("versions"):
        local("mkdir versions")
    local("tar -czf versions/web_static_{}.tgz web_static".
          format(str(datetime.now()).split(".")[0].replace("-", "").
                 replace(" ", "").replace(":", "")))


def do_deploy(archive_path):
    """Method do_deploy """
    if not path.exists(archive_path):
        return(False)

    try:
        put(archive_path, "/tmp/")

        tgzname = archive_path.split("/")[-1]
        webpath = "/data/web_static/releases/{}/".format(tgzname[:-4])
        tmpath = "/tmp/{}".format(tgzname)
        sympath = "/data/web_static/current"

        run("mkdir -p {}".format(webpath))

        run("tar -xzf {} -C {}".format(tmpath, webpath))

        run("rm {}".format(tmpath))

        run("mv {}web_static/* {}".format(webpath, webpath))

        run("rm -rf {}/web_static".format(webpath))

        run("rm -rf {}".format(sympath))

        run("ln -s {} {}".format(webpath, sympath))
        return(True)

    except:
        return(False)
