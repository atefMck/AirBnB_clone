#!/usr/bin/python3
"""
Unit Test for filestorage
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Tests the file storage
    """
    def setUp(self):
        """
        Sets up an instance of storage
        """
        self.storage = FileStorage()
        self.storage._refresh()
        self.storage.reload()

    def testTheirs(self):
        """
        testcase
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        test_dict = my_model.to_dict()
        new_model = BaseModel(**test_dict)
        self.assertEqual(new_model.id, my_model.id)

    def testAll(self):
        """
        Tests if all returns a dict
        """
        dic = self.storage.all()
        self.assertEqual(type(dic), dict)

    def testAllValue(self):
        """
        Tests al()
        """
        self.assertEqual(self.storage.all(), {})

    def testSaveEmpty(self):
        """
        Tests if save wrote to the file an empty dict
        """
        self.storage.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            self.r = f.read()
            self.assertEqual(self.r, "{}")

    def testSave(self):
        base = BaseModel()
        pre_obj = self.storage.all()
        self.storage.save()
        after_obj = self.storage.all()
        self.assertEqual(pre_obj, after_obj)

    def testNew(self):
        """
        tests storage
        """
        self.base = BaseModel()
        self.base.id = '121212'
        self.storage.new(self.base)
        test_dic = self.storage.all()
        self.assertTrue(test_dic['BaseModel.121212'])

    @unittest.expectedFailure
    def testNew_class_BaseModel(self):
        """
        tests new
        """
        self.storage.new([])

    def testReload(self):
        """
        test reload
        """
        self.test_dictionary = {"BaseModel.121212": {"id": 121212}}
        self.test_dictionary["BaseModel.221212"] = {"id": 121212}
        with open("file.json", 'w+') as f:
            json.dump(self.test_dictionary, f)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 2)

    def testReload_no_existing_file(self):
        """
        tests reload with no existing file
        """
        if os.path.isfile('file.json'):
            os.remove('file.json')
        self.storage.reload()
        self.assertFalse(os.path.isfile('file.json'))

    def testPrivate(self):
        """
        test if exist a private variables
        """
        with self.assertRaises(AttributeError):
            FileStorage.__file_path

    def testPrivateO(self):
        """
        test if exist a private variables
        """
        with self.assertRaises(AttributeError):
            FileStorage.__objects
