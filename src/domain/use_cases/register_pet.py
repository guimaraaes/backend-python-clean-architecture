from abc import ABC, abstractclassmethod
from typing import Dict

from src.domain.models import Pets


class RegisterPet(ABC):
    """interface to FindPet use case"""

    @abstractclassmethod
    def registry(
        clc, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """use case"""

        raise Exception("should implement method: registry")
