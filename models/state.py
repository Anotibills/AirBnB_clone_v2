#!/usr/bin/python3
""" Script for state module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, MetaData
from models.city import City
from sqlalchemy.orm import relationship, backref
from models import storage
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
    else

        @property
        def cities(self):
            """ Getter attribute for cities in FileStorage """  
            all_cities = models.storage.all(City)
            state_cities = []
            for city_ins in all_cities.values():
                if city_ins.state_id == self.id:
                    state_cities.append(city_ins)

            return state_cities
