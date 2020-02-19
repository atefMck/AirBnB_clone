#!/usr/bin/python3
""" This module contains base class for all classes """
import uuid
import datetime
import models


class BaseModel():
    """docstring for BaseModel"""

    def __init__(self, *args, **kwargs):
        """docstring for init method of BaseModel"""
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
            self.created_at = datetime.datetime.strptime(
                self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.datetime.strptime(
                self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self):
        """docstring for __str__ method of BaseModel"""

        string = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return (string)

    def save(self):
        """saves updated class to storage"""

        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        newdict = dict(self.__dict__)
        newdict['__class__'] = self.__class__.__name__
        newdict['created_at'] = str(
            self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        newdict['updated_at'] = str(
            self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        return (newdict)
