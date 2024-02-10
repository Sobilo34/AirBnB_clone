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
        print("Printing self.__object")
        print(self.__object)
        for key, obj in self.__object.items():
            print("Print obj.to_dict() method")
            print(obj.to_dict())
            json_dict[key] = obj.to_dict()
            
        try:
            with open(FileStorage.__file_path, "w") as file:
                print("Try to create file")
                print(json_dict)
                json.dump(json_dict, file)
        except Exception as e:
            print(f"Error saving file: {e}")


    def reload(self):
        """Deserialize object from __file_path"""
        try:
            with open(FileStorage.__file_path) as file:
                json_dict = json.load(file)
                for obj_dict in json_dict.values():
                    obj_name = obj_dict.get("__name__")
                    if obj_name:
                        del obj_dict.get["__name__"]
                        self.new(eval(obj_name)(**obj_dict))
            
        except FileNotFoundError:
            print(f"File '{FileStorage.__file_path}' not found.")
