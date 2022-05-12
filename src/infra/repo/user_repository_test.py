from faker import Faker
from src.infra.config import DBConnectionHandler

from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection = DBConnectionHandler()


def test_insert_user():
    """should insert user"""
    name = faker.name()
    password = faker.word()
    engine = db_connection.get_engine()

    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute("SELECT * FROM users WHERE id='{}';".format(new_user.id)).fetcheone()

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))
