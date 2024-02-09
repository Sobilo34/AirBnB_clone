#!/usr/bin/env python3

import models
import uuid
import datetime


class BaseModel():
    """ Class that defines all common attributes"""
    def __init__(self, *args, **kwargs):
        """Initalizes instances of the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key not in self.__dict__ and key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()


    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print(
                "\t{}: ({}) - {}".format(
                    key,
                    type(my_model_json[key]),
                    my_model_json[key])
                )
    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
    model_3 = my_model
    print(my_model is model_3)
