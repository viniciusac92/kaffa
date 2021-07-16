from app.custom_errors import required_key
from app.custom_errors.not_found import NotFoundError

from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ManagerModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class ManagerServices:

    required_fields = ["name", "cpf", "id_user"]

    @staticmethod
    def create_manager(data: dict):

        if verify_missing_key(data, ManagerServices.required_fields):
            raise MissingKeyError(data, ManagerServices.required_fields)

        if verify_recieved_keys(data, ManagerServices.required_fields):
            raise RequiredKeyError(data, ManagerServices.required_fields)

        manager = ManagerModel(**data)

        add_commit(manager)

        return get_one(ManagerModel, manager.id)

    @staticmethod
    def get_all_managers():

        return get_all(ManagerModel)

    @staticmethod
    def get_by_id(id):

        return get_one(ManagerModel, id)

    @staticmethod
    def update_manager(data: dict, id):

        if verify_recieved_keys(data, ManagerServices.required_fields):
            raise RequiredKeyError(data, ManagerServices.required_fields)

        if not get_one(ManagerModel, id):
            raise NotFoundError

        manager = get_one(ManagerModel, id)
        update_model(manager, data)

        return get_one(ManagerModel, id)

    @staticmethod
    def delete_manager(id: int) -> None:

        if not get_one(ManagerModel, id):
            raise NotFoundError

        manager = get_one(ManagerModel, id)
        delete_commit(manager)
