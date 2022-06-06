from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import UserRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterPetController


def register_user_composer() -> RouteInterface:
    """composing register user route
    :param - none
    : return - object eith register user route
    """

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterPetController(use_case)

    return register_user_route
