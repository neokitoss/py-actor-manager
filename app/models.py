from dataclasses import dataclass


class Actor:
    def __init__(self, _id: int, first_name: str, last_name: str):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
