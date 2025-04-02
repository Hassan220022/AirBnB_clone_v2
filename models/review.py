#!/usr/bin/python3
"""
Contains the Review class model
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """
    Represents a review for a MySQL database
    Inherits from SQLAlchemy Base and links to the MySQL table reviews
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store reviews
        text (sqlalchemy.String): The review text
        place_id (sqlalchemy.String): The place id of the review
        user_id (sqlalchemy.String): The user id of the review
    """
    __tablename__ = 'reviews'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = "" 