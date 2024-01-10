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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """
        string representation of the obj
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """
        update the Updated_at field
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """
        returns a dictionary representation of 
        the obj
        """
        my_dict = {}
        for k, v in self.__dict__.items():
            if k == "updated_at" or k == "created_at":
                my_dict[k] = v.isoformat()
            else:
                my_dict[k] = v
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
