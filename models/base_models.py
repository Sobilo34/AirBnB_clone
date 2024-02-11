#!/usr/bin/env python3
"""Module defines all common attributes/methods for other classes"""
import models
import uuid
import datetime
from models import storage

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initalizes instances of the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    datetime_obj = (
                        datetime.datetime.strptime(value, TIME_FORMAT))
                    self.__dict__[key] = datetime_obj
                elif key not in self.__dict__ and key != "__class__":
                    self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """String representation of Class instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save an updated model instance."""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Converts instance attributes to a dictionary."""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict


if __name__ == "__main__":
    # my_model = BaseModel()
    # my_model.name = "My_First_Model"
    # my_model.my_number = 89
    # print(my_model.id)
    # print(my_model)
    # print(type(my_model.created_at))
    # print("--")
    # my_model_json = my_model.to_dict()
    # print(my_model_json)
    # print("JSON of my_model:")
    # for key in my_model_json.keys():
    #     print(
    #             "\t{}: ({}) - {}".format(
    #                 key,
    #                 type(my_model_json[key]),
    #                 my_model_json[key])
    #             )
    # print("--")
    # my_new_model = BaseModel(**my_model_json)
    # print(my_new_model.id)
    # print(my_new_model)
    # print(type(my_new_model.created_at))

    # print("--")
    # print(my_model is my_new_model)
    # model_3 = my_model
    # print(my_model is model_3)
    from models import storage
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
