from abc import ABC, abstractclassmethod
from typing import Dict

from src.domain.models import Users


class RegisterUser(ABC):
    """intergace to RegisterUSer use case"""

    @abstractclassmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """case"""
        raise Exception("should implement method: register")
