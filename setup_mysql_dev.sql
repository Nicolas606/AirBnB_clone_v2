-- CREATE USERS AND DATA BASES TO HOLBERTON SCHOOL PROJECT --
CREATE database IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pw';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* to hbnb_dev@localhost;
GRANT SELECT ON performance_schema . * TO hbnb_dev@localhost;
