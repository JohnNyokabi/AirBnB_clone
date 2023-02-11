#!/usr/bin/python3
"""
Amenity class representing new amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity subclass inheriting from BaseModel """
    name = ""
