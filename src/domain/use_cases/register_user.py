from abc import ABC, abstractclassmethod
from typing import Dict

from src.domain.models import Users


class RegisterUser(ABC):
    """intergace to RegisterUSer use case"""

    @abstractclassmethod
    def registry(cls, name: str, password: str) -> Dict[bool, Users]:
        """use case"""
        raise Exception("should implement method: register")
