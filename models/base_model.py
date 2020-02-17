#!/usr/bin/python3
""" This module contains base class for all classes """
import uuid
import datetime

class BaseModel():
	"""docstring for BaseModel"""

	def __init__(self):
		"""docstring for init method of BaseModel"""

		self.id = str(uuid.uuid4())
		self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()

	def __str__(self):
		"""docstring for __str__ method of BaseModel"""

		string = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
		return (string)

	def save(self):
		"""saves updated class to storage"""

		self.updated_at = datetime.datetime.now()

	def to_dict(self):
		"""returns a dictionary containing all keys/values of __dict__"""

		self.__dict__['__class__'] = self.__class__.__name__
		self.created_at = str(self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
		self.updated_at = str(self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
		return (self.__dict__)
