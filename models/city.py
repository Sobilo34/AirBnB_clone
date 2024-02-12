#!/usr/bin/python3

"""A City class inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """A City class that inherits from BaseModel
    """
    state_id: str = ""
    name: str = ""
