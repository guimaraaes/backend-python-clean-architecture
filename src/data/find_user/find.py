from typing import Dict, List, Type

from src.data.interfaces import UsersRepositoryInterface as UserRepository
from src.domain.models import Users
from src.domain.use_cases import FindUser as FindUserInterface


class FindUser(FindUserInterface):
    """class to define use case Find User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """select user by id
        :param - user_id: id of the user
        :param - dictionary with informations of the process
        """
        response = None
        validate_entry = isinstance(user_id, int)
        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)
        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """select user by name
        :param - name: name of the user
        :param - dictionary with informations of the process
        """
        response = None
        validate_entry = isinstance(name, str)
        if validate_entry:
            response = self.user_repository.select_user(name=name)
        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """select user by id and name
        :param - user_id: id of the user
        :param - name: name of the user
        :param - dictionary with informations of the process
        """
        response = None
        validate_entry = isinstance(name, str) and isinstance(user_id, int)
        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=name)
        return {"Success": validate_entry, "Data": response}
