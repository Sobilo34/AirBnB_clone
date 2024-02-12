#!/usr/bin/env python3
"""Helps recreate BaseModel class from a dictionary representation."""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """Serializes instances to a JSON file and deserializes
JSON file to instances.
    """

    __file_path = "file.json"
    __object = {}
    __class_list = {
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__object

    def new(self, obj):
        """Sets in __objects the obj with <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__object[key] = obj

    def save(self):
        """Save __objects to a JSON file in __file_path"""
        json_dict = {}
        for key, obj in self.__object.items():
            json_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserialize object from __file_path"""
        try:
            with open(FileStorage.__file_path) as file:
                json_dict = json.load(file)
                for key, obj_dict in json_dict.items():
                    obj_name = obj_dict.pop("__class__", "BaseModel")
                    obj_list = FileStorage.__class_list.get(obj_name, BaseModel)
                    self.new(obj_list(**obj_dict))
        except FileNotFoundError:
            pass
