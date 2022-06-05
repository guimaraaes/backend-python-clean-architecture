from faker import Faker
from src.data.test import FindPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest

from .find_pet_controller import FindPetController

faker = Faker()


def test_handle_user_id():
    """testing handle method"""
    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(
        query={
            "user_id": faker.random_number(),
        }
    )
    response = find_pet_controller.handle(http_request)

    assert (
        find_pet_use_case.by_user_id_param["user_id"] == http_request.query["user_id"]
    )

    assert response.status_code == 200
    assert response.body


def test_handle_user_id_and_pet_id():
    """testing handle method"""
    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "pet_id": faker.random_number()}
    )
    response = find_pet_controller.handle(http_request)

    assert (
        find_pet_use_case.by_pet_id_and_user_id_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_pet_use_case.by_pet_id_and_user_id_param["pet_id"]
        == http_request.query["pet_id"]
    )

    assert response.status_code == 200
    assert response.body


def test_handle_no_query_param():
    """testing handle method with no query param"""
    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest()

    response = find_pet_controller.handle(http_request)

    assert find_pet_use_case.by_user_id_param == {}
    assert find_pet_use_case.by_pet_id_param == {}
    assert find_pet_use_case.by_pet_id_and_user_id_param == {}

    assert response.status_code == 400
    assert "error" in response.body
