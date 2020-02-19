#!/usr/bin/python3
""" This module contains the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """docstring for Review class"""
    
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """docstring for init method of Review"""
        super().__init__(*args, **kwargs)
