#!usr/bin/python3
"""
test base_model.py
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel """
    def setUp(self):
        self.base = BaseModel()

    def testId(self):
        """ Test id"""
        self.assertEqual(type(self.base.id), str)

    def testLen(self):
        """ Test length of id """
        self.assertEqual(len(self.base.id), 36)
