"""
This module contains the `Person` class. 

Examples:
    >>> p = Person("Jane Doe", 32, "123 Main St.")
    >>> print(p)
    Jane Doe, 32, 123 Main St.
"""

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_info(self, name=None, age=None, address=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if address:
            self.address = address

    def __str__(self):
        return f"{self.name}, {self.age}, {self.address}"
