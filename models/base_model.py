#!/usr/bin/python3
"""
Base model from which oyther models will inherites
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model
    """
    def __init__(self):
        id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()


    def __str__(self):
        pass


    def save(self):
        pass


    def to_dict(self):
        pass
