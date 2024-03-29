from typing import List

from src.domain.models import Users
from src.domain.test import mock_users


class UserRepositorySpy:
    """spy to User Repository"""

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, password: str) -> Users:
        """spy to all the atributes"""
        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password
        return mock_users()

    def select_user(self, user_id=None, name: str = None) -> List[Users]:
        """spy to all the atributes"""
        self.select_user_params["user_id"] = user_id
        self.select_user_params["name"] = name

        return [mock_users()]
