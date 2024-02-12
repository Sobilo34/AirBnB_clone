#!/usr/bin/python3

"""User Module:
A class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class User that inherits from BaseModel"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    # def __init__(self):
    #     """Class initialization."""
    #     super().__init__()
    #     self.email = User.email
    #     self.password = User.password
    #     self.first_name = User.first_name
    #     self.last_name = User.last_name

    # def __str__(self):
    #     """String representation of Class instance."""
    #     str_repr = "[{}] ({}) {}".format(
    #             self.__class__.__name__, self.id, self.__dict__)
    #     return str_repr

    # def to_dict(self):
    #     """Converts instance attributes to a dictionary."""
    #     my_dict = self.__dict__.copy()
    #     my_dict["__class__"] = self.__class__.__name__
    #     my_dict["created_at"] = my_dict["created_at"].isoformat()
    #     my_dict["updated_at"] = my_dict["updated_at"].isoformat()
    #     return my_dict
