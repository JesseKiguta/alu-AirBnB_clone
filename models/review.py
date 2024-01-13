"""
review model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Model that inherits from BaseModel"""
    place_id = ''
    user_id = ''
    text = ''
