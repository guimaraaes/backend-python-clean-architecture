from src.data.find_pet import FindPet
from src.infra.repo.pet_repository import PetRepository
from src.presenters.controllers import FindPetController


def find_pet_composer() -> FindPetController:
    """composing find pet route
    :param - none
    :return - object with find pet route
    """

    repository = PetRepository()
    use_case = FindPet(repository)
    find_pet_route = FindPetController(use_case)

    return find_pet_route
