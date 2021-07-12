from flask_sqlalchemy.model import Model
from ipdb import set_trace
from . import db

def verify_missing_key(data: dict, required_keys: list) -> list:
    data_keys = data.keys()

    return [key for key in required_keys if key not in data_keys]

def verify_recieved_keys(data:dict,key_list:list) -> list:
    data_keys = data.keys()

    return [key for key in data_keys if key not in key_list]

def add_all_commit(list_model: list[Model]) -> None:
    db.session.add_all(list_model)
    db.session.commit()

def add_commit(model:Model) -> None:
    db.session.add(model)
    db.session.commit()

def delete_commit(model:Model) -> None:
    db.session.delete(model)
    db.session.commit()

def get_all(model:Model):
    return db.session.query(model).all()

def get_one(model:Model, id: int):
    return model.query.get(id)

def update_model(model:Model, data:dict) -> None:
    for key, value in data.items():
        setattr(model, key, value)
    add_commit(model)


