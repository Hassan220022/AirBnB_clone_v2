#!/usr/bin/python3
"""
Contains the State class model
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """
    Represents a state for a MySQL database
    Inherits from SQLAlchemy Base and links to the MySQL table states
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States
        name (sqlalchemy.String): The name of the State
        cities (sqlalchemy.orm.relationship): The State-City relationship
    """
    __tablename__ = 'states'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""
        
        @property
        def cities(self):
            """
            Returns the list of City objects with state_id equals to the current State.id
            """
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list 