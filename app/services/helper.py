from app.configs.database import db
from faker import Faker
from flask_sqlalchemy.model import Model
from ipdb import set_trace

fake = Faker()


def verify_missing_key(data: dict, required_keys: list) -> list:
    data_keys = data.keys()

    return [key for key in required_keys if key not in data_keys]


def verify_recieved_keys(data: dict, key_list: list) -> list:
    data_keys = data.keys()

    return [key for key in data_keys if key not in key_list]


def add_all_commit(list_model: list[Model]) -> None:
    db.session.add_all(list_model)
    db.session.commit()


def add_commit(model: Model) -> None:
    db.session.add(model)
    db.session.commit()


def delete_commit(model: Model) -> None:
    db.session.delete(model)
    db.session.commit()


def get_all(model: Model):
    return db.session.query(model).all()


def get_one(model: Model, id: int):
    return model.query.get(id)


def update_model(model: Model, data: dict) -> None:
    for key, value in data.items():
        setattr(model, key, value)
    add_commit(model)


def create_fake_user(amount: int):
    return {
        "username": fake.first_name(),
        "type": fake.random_int(min=1, max=3),
        "password": str(fake.password(length=4, digits=True)),
        "name": fake.name(),
        "cpf": str(fake.random_number(digits=9, fix_len=True)),
    }


def create_fake_product(amount: int):
    return {
        "name": fake.name(),
        "description": fake.sentence(nb_words=10, variable_nb_words=False),
        "price": fake.pyfloat(
            left_digits=2, right_digits=2, positive=True, max_value=100
        ),
        "stock": fake.random_number(digits=2, fix_len=True),
    }
