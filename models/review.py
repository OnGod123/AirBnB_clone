#!/usr/bin/python3
"""
Defines review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User's reviews about a place"""
    place_id = ""
    user_id = ""
    text = ""
