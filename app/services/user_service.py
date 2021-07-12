from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import UserModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)
from ipdb import set_trace

class UserServices:

    required_fields = ["username", "tipo", "password"]

    @staticmethod
    def create_user(data:dict):

        if verify_missing_key(data,UserServices.required_fields):
            raise MissingKeyError(data, UserServices.required_fields)

        if verify_recieved_keys(data, UserServices.required_fields):
            raise RequiredKeyError(data, UserServices.required_fields)

        password_to_hash = data.pop('password')
        usuario = UserModel(**data)
        usuario.password = password_to_hash

        add_commit(usuario)
        
        return get_one(UserModel, usuario.id)

    @staticmethod
    def get_all_users():

        return get_all(UserModel)

    @staticmethod
    def update_user(data: dict, id):

        if verify_recieved_keys(data, UserServices.required_fields):
            raise RequiredKeyError(data, UserServices.required_fields)
        
        if not get_one(UserModel, id):
            raise NotFoundError

        usuario = get_one(UserModel,id)
        update_model(usuario, data)

        return get_one(UserModel, id)

    @staticmethod
    def delete_user(id: int) -> None:

        if not get_one(UserModel, id):
            raise NotFoundError

        usuario = get_one(UserModel,id)
        delete_commit(usuario)

    @staticmethod
    def found_user(username):
        return UserModel.query.filter_by(username=username).first()

    @staticmethod
    def get_by_id(id):
        user = get_one(UserModel, id)
        if not user:
            raise NotFoundError

        return user
