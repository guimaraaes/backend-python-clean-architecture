from src.data.find_user import FindUser
from src.infra.repo.user_repository import UserRepository
from src.presenters.controllers import FindUserController


def find_user_composer() -> FindUserController:
    """composing find user route
    :param - none
    :return - object with find user route
    """

    repository = UserRepository()
    use_case = FindUser(repository)
    find_user_route = FindUserController(use_case)

    return find_user_route
