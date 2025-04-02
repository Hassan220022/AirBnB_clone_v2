#!/usr/bin/python3
"""
Contains the Amenity class model
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Represents an amenity for a MySQL database
    Inherits from SQLAlchemy Base and links to the MySQL table amenities
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store amenities
        name (sqlalchemy.String): The name of the amenity
    """
    __tablename__ = 'amenities'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = "" 