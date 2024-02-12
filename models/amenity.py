#!/usr/bin/python3

"""An amenity class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name: str = ""
