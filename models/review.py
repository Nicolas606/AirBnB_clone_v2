#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """

    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
