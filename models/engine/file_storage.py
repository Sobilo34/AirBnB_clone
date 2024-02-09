#!/usr/bin/env python3

import json


class FileStorage:
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

        for key, obj in FileStorage.__object.items():
            json_dict[key] = obj.to_dict()
            

        with open(FileStorage.__file_path, "w") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserialize object from __file_path"""
        try:
            with open(FileStorage.__file_path) as file:
                json_dict = json.load(file)
                for obj_dict in json_dict.values():
                    obj_name = obj_dict["__name__"]
                    del obj_dict["__name__"]
                    self.new(eval(obj_name)(**obj_dict))
            
        except FileNotFoundError:
            pass
