# pylint: disable=401
# from string import digits

from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel
from src.infra.entities.pets import AnimalTypes

from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection = DBConnectionHandler()


def test_insert_pet():
    """should insert pet"""
    name = faker.name()
    specie = "dog"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    engine = db_connection.get_engine()

    new_pet = pet_repository.insert_pet(name, specie, age, user_id)
    query_pet = engine.execute(
        "SELECT * FROM pets WHERE id='{}';".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id

    engine.execute("DELETE FROM pets WHERE id='{}'".format(new_pet.id))


def test_select_pet():
    """shoul select a pet in Pets table and compare it"""
    pet_id = faker.random_number(digits=5)
    name = faker.name()
    specie = "dog"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    data = PetsModel(
        id=pet_id, name=name, specie=AnimalTypes("dog"), age=age, user_id=user_id
    )

    engine = db_connection.get_engine()
    engine.execute(
        "INSERT INTO pets (id, name, specie, age, user_id) VALUES('{}', '{}', '{}', '{}', '{}');".format(
            pet_id, name, specie, age, user_id
        )
    )
    query_user1 = pet_repository.select_pet(pet_id=pet_id)
    query_user2 = pet_repository.select_pet(user_id=user_id)
    query_user3 = pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    engine.execute("DELETE FROM pets WHERE id='{}';".format(pet_id))
