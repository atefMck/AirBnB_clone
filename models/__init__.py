#!/usr/bin/python3
""" This is the init file for all models """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
