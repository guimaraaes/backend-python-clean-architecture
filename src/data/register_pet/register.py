from typing import Dict, List, Type

from src.data.find_user import FindUser
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets, Users
from src.domain.use_cases import RegisterPet as RegisterPetInterface


class RegisterPet(RegisterPetInterface):
    """class to define use case: Register Pet"""

    def __init__(self, pet_repository: Type[PetRepository], find_user: Type[FindUser]):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Register Pet
        :param  - name: pet name
                - specie: type of the specie
                - age: age of the pet
                - user_information: Dictionary with user_id and/or user_name
        :return - Dictionary with information of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name, specie, age, user_information["user_id"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """check user infos and select user
        :param - user_information: dictionary with user_id and/or user_name
        :return - dictionaty with the response of find_user use case
        """

        user_founded = None
        user_params = user_information.keys()
        if "user_id" in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_id_and_name(
                user_information["user_id"], user_information["user_name"]
            )
        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_name(user_information["user_name"])
        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = self.find_user.by_id(user_information["user_id"])
        else:
            return {"Success": False, "Data": None}

        return user_founded
