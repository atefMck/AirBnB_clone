#!/usr/bin/python3
""" This module contains the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """docstring for City class"""

    def __init__(self, *args, **kwargs):
        """docstring for init method of City"""
        super(City, self).__init__(*args, **kwargs)
        self.City_id = self.id
        self.name = ""
