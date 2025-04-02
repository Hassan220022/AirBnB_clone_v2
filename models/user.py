#!/usr/bin/python3
"""
Contains the User class model
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Represents a user for a MySQL database
    Inherits from SQLAlchemy Base and links to the MySQL table users
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store users
        email (sqlalchemy.String): The email of the user
        password (sqlalchemy.String): The password of the user
        first_name (sqlalchemy.String): The first name of the user
        last_name (sqlalchemy.String): The last name of the user
    """
    __tablename__ = 'users'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = "" 