#!/usr/bin/python3

"""A state class inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """A state class that inherits from BaseModel."""
    name: str = ""
