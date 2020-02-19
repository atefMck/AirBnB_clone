#!/usr/bin/python3
""" This module contains the state class """
from models.base_model import BaseModel


class State(BaseModel):
    """docstring for state class"""
    
    name = ""

    def __init__(self, *args, **kwargs):
        """docstring for init method of state"""
        super().__init__(*args, **kwargs)
