#!/usr/bin/python3
"""
User clsaa
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Public attribute of user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
