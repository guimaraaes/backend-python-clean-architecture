from faker import Faker
from src.infra.test import PetRepositorySpy

from .find import FindPet

faker = Faker()


def test_by_pet_id():
    """testind by_pet_id method"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]
    assert response["Success"] is True
    assert response["Data"]


def test_by_user_id():
    """testind by_user_id method"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_pet.by_user_id(user_id=attributes["user_id"])

    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_and_user_id():
    """testind by_pet_id_and_user_id method"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "pet_id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }

    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], user_id=attributes["user_id"]
    )

    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]
    assert response["Success"] is True
    assert response["Data"]
