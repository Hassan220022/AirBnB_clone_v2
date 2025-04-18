#!/usr/bin/python3
"""
Contains the City class model
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Represents a city for a MySQL database
    Inherits from SQLAlchemy Base and links to the MySQL table cities
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities
        name (sqlalchemy.String): The name of the City
        state_id (sqlalchemy.String): The state id of the City
    """
    __tablename__ = 'cities'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete-orphan")
    else:
        state_id = ""
        name = "" 