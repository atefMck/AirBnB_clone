#!/usr/bin/python3
""" This module contains the user class """
from models.base_model import BaseModel

class User(BaseModel):
    """docstring for User class"""

    def __init__(self):
        """docstring for init method of User"""
        email = ""
        password = ""
        firstname = ""
        lastname = ""
