#!/usr/bin/python3
""" This module contains the Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """docstring for Amenity class"""

    def __init__(self, *args, **kwargs):
        """docstring for init method of Amenity"""
        super(Amenity, self).__init__(*args, **kwargs)
        self.name = ""
