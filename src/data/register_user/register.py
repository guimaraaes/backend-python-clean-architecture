from typing import Dict, Type

from src.data.interfaces import UsersRepositoryInterface as UserRepository
from src.domain.models import Users
from src.domain.use_cases import RegisterUser as RegisterUserInterface


class RegisterUser(RegisterUserInterface):
    """class to define usercase: Register User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user use case
        :param  - name: person name
                - password: password of the person
        :return - distionary with informations of the process
        """
        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)
        if validate_entry:
            response = self.user_repository.insert_user(name, password)
        return {"Success": validate_entry, "Data": response}
