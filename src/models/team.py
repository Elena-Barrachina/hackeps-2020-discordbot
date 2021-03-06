#!/usr/bin/python3
from typing import Optional, List


class Team:
    def __init__(self, name: str, users: Optional[List[int]] = None, role_id: Optional[int] = None):
        if users is None:
            users = []
        self.name = name
        self.members = users
        self.role_id = role_id

    def add_user(self, user: int):
        self.members.append(user)

    def size(self):
        return len(self.members)
