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
