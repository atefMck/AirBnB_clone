#!/usr/bin/python3
""" This module contains storage handling class """

import json
import os

class FileStorage():
	"""docstring for FileStorage"""

	def __init__(self):
		"""docstring for init method of FileStorage"""

		self.__file_path = "file.json"
		self.__objects = dict()

	def all(self):
		""" returns all objects in file """

		return (self.__objects)

	def new(self, obj):
		""" adds new object to dict """

		key = obj.__class__.__name__ + "." + obj.id
		self.__objects[key] = obj.to_dict()

	def save(self):
		""" saves objects to json file """

		json_obj = json.dumps(self.__objects)
		with open(self.__file_path, 'w') as file:
			file.write(json_obj)

	def reload(self):
		""" reloads all objects from file """

		if os.path.isfile(self.__file_path):
			with open(self.__file_path, 'r') as file:
				json_text = file.read()
			self.__objects = json.loads(json_text)
