"""
This module contains the pydantic example for mypy. 

Examples:
    >>> m = Model(age=42, list_of_ints=[1, '2', b'3'])
    >>> print(m.middle_name)  # not a model field!
    >>> Model()  # will raise a validation error for age and list_of_ints
"""

from datetime import datetime
from pydantic import BaseModel, NoneStr

class Model(BaseModel):
    """
    This is the pydantic example for mypy.

    Attributes:
        age: the age of the model
        first_name: the first name of the model
        last_name: the last name of the model
        signup_ts: the timestamp of the model's signup
        list_of_ints: a list of integers
    """
    age: int
    first_name = 'Merlinus'
    last_name: NoneStr = None
    signup_ts: datetime | None = None
    list_of_ints: list[int]