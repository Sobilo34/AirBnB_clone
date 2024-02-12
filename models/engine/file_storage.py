#!/usr/bin/env python3
"""Helps recreate BaseModel class from a dictionary representation."""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes
JSON file to instances.
    """

    __file_path = "file.json"
    __object = {}

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
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review

        try:
            with open(FileStorage.__file_path) as file:
                json_dict = json.load(file)
                for key, obj_dict in json_dict.items():
                    obj_name = key.split(".")[0]

                    if obj_name == "User":
                        model = User(**obj_dict)
                    elif obj_name == "Amenity":
                        model = Amenity(**obj_dict)
                    elif obj_name == "State":
                        model = State(**obj_dict)
                    elif obj_name == "City":
                        model = City(**obj_dict)
                    elif obj_name == "Place":
                        model = Place(**obj_dict)
                    elif obj_name == "Review":
                        model = Review(**obj_dict)
                    else:
                        model = BaseModel(**obj_dict)
        except FileNotFoundError:
            pass
