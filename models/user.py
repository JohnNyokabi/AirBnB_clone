#!/usr/bin/python3
""" User class for new users """
from models.base_model import BaseModel


class User(BaseModel):
    """ User subclass inheriting from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
