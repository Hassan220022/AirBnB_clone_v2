#!/usr/bin/python3
"""
Contains the Place class model
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    """
    Represents a place for a MySQL database
    Inherits from SQLAlchemy Base and links to the MySQL table places
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store places
        city_id (sqlalchemy.String): The city id of the place
        user_id (sqlalchemy.String): The user id of the place
        name (sqlalchemy.String): The name of the place
        description (sqlalchemy.String): The description of the place
        number_rooms (sqlalchemy.Integer): The number of rooms in the place
        number_bathrooms (sqlalchemy.Integer): The number of bathrooms in the place
        max_guest (sqlalchemy.Integer): The maximum number of guests allowed
        price_by_night (sqlalchemy.Integer): The price of the place per night
        latitude (sqlalchemy.Float): The latitude of the place
        longitude (sqlalchemy.Float): The longitude of the place
        amenity_ids (list): A list of amenity ids
    """
    __tablename__ = 'places'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = [] 