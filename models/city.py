#!/usr/bin/python3
"""
The city class representing new city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ city subclass that inherits from BaseModel"""
    state_id = ""
    name = ""
