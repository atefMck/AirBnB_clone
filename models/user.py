#!/usr/bin/python3
""" This module contains the user class """
from models.base_model import BaseModel


class User(BaseModel):
    """docstring for User class"""

    def __init__(self, *args, **kwargs):
        """docstring for init method of User"""
        super(User, self).__init__(*args, **kwargs)
        email = ""
        password = ""
        firstname = ""
        lastname = ""
