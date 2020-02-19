#!/usr/bin/python3
""" This module contains the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """docstring for City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """docstring for init method of City"""
        super().__init__(*args, **kwargs)
