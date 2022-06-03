from abc import ABC, abstractclassmethod
from typing import Dict, List

from src.domain.models import Pets


class FindPet(ABC):
    """interface to FindPet use case"""

    @abstractclassmethod
    def by_pet_id(cls, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specifc case"""
        raise Exception("should implement method: by_pet_id")

    @abstractclassmethod
    def by_user_id(cls, user_id: int) -> Dict[bool, List[Pets]]:
        """Specifc case"""
        raise Exception("should implement method: by_user_id")

    @abstractclassmethod
    def by_pet_id_and_user_id(cls, user_id: int, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specifc case"""
        raise Exception("should implement method: by_pet_id_and_user_id")
