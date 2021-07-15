from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import UserModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)
from app.services.waiter_service import WaiterServices
from app.services.manager_service import ManagerServices
from app.services.operator_service import OperatorServices
from ipdb import set_trace


class UserServices:

    required_fields = ["username", "type", "password", "name", "cpf"]

    @staticmethod
    def create_user(data: dict):

        if verify_missing_key(data, UserServices.required_fields):
            raise MissingKeyError(data, UserServices.required_fields)

        if verify_recieved_keys(data, UserServices.required_fields):
            raise RequiredKeyError(data, UserServices.required_fields)

        name = data.pop('name')
        cpf = data.pop('cpf')
        password_to_hash = data.pop('password')
        user = UserModel(**data)
        user.password = password_to_hash

        add_commit(user)

        user = get_one(UserModel, user.id)

        if data["type"] == 1:
            info_user = ManagerServices.create_manager(
                {"name": name, "cpf": cpf, "id_user": user.id})

        if data["type"] == 2:
            info_user = WaiterServices.create_waiter(
                {"name": name, "cpf": cpf, "id_user": user.id})

        if data["type"] == 3:
            info_user = OperatorServices.create_operator(
                {"name": name, "cpf": cpf, "id_user": user.id})

        if user.type == 1:
            type = "Manager"
        elif user.type == 2:
            type = "Waiter"
        else:
            type = "Cashier"

        return {
            "name": info_user.name,
            "type": type,
            "username": user.username,
            "cpf": info_user.cpf,
            "password": user.password_hash
        }

    @staticmethod
    def get_all_users():

        return get_all(UserModel)

    @staticmethod
    def update_user(data: dict, id):

        if verify_recieved_keys(data, UserServices.required_fields):
            raise RequiredKeyError(data, UserServices.required_fields)

        if not get_one(UserModel, id):
            raise NotFoundError

        user = get_one(UserModel, id)
        update_model(user, data)

        return get_one(UserModel, id)

    @staticmethod
    def delete_user(id: int) -> None:

        if not get_one(UserModel, id):
            raise NotFoundError

        user = get_one(UserModel, id)
        delete_commit(user)

    @staticmethod
    def found_user(username):
        return UserModel.query.filter_by(username=username).first()

    @staticmethod
    def get_by_id(id):
        user = get_one(UserModel, id)
        if not user:
            raise NotFoundError

        return user
