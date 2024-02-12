#!/usr/bin/env python3
"""Module defines all common attributes/methods for other classes"""
import models
import uuid
import datetime

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
        from models import storage
        """Save an updated model instance."""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Converts instance attributes to a dictionary."""
        my_dict = self.__dict__.copy()
        # my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
