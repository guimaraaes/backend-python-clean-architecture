from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import UserRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterUserController


def register_user_composer() -> RouteInterface:
    """composing register user route
    :param - none
    : return - object with register user route
    """

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
