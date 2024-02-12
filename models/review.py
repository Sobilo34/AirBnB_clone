#!/usr/bin/python3

"""A review class inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A review class that inherits from BaseModel."""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
