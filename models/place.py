#!/usr/bin/python3
""" This module contains the Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """docstring for Place class"""

    def __init__(self, *args, **kwargs):
        """docstring for init method of Place"""

        super(Place, self).__init__(*args, **kwargs)
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
