#!/usr/bin/python3
""" This module contains base class for all classes """
import uuid
import datetime

class BaseModel():
	"""docstring for BaseModel"""

	def __init__(self, *args, **kwargs):
		"""docstring for init method of BaseModel"""
		if kwargs:
			for key in kwargs:
				if key != "__class__":
					self.__dict__[key] = kwargs[key]
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.datetime.now()
			self.updated_at = datetime.datetime.now()
		if type(self.created_at) is str:
			self.created_at = datetime.datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
		if type(self.updated_at) is str:
			self.updated_at = datetime.datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

	def __str__(self):
		"""docstring for __str__ method of BaseModel"""

		string = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
		return (string)

	def save(self):
		"""saves updated class to storage"""

		self.updated_at = datetime.datetime.now()

	def to_dict(self):
		"""returns a dictionary containing all keys/values of __dict__"""

		newdict = dict(self.__dict__)
		newdict['__class__'] = self.__class__.__name__
		newdict['created_at'] = str(self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
		newdict['updated_at'] = str(self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
		return (newdict)


my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)