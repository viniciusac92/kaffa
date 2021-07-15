from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import OperatorModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)


class OperatorServices:

    required_fields = ["name", "cpf", "id_user"]

    @staticmethod
    def create_operator(data: dict):

        if verify_missing_key(data, OperatorServices.required_fields):
            raise MissingKeyError(data, OperatorServices.required_fields)

        if verify_recieved_keys(data, OperatorServices.required_fields):
            raise RequiredKeyError(data, OperatorServices.required_fields)

        operator = OperatorModel(**data)

        add_commit(operator)

        return get_one(OperatorModel, operator.id)

    @staticmethod
    def get_all_operatores():

        return get_all(OperatorModel)

    @staticmethod
    def get_by_id(id):

        return get_one(OperatorModel, id)

    @staticmethod
    def update_operator(data: dict, id):

        if verify_recieved_keys(data, OperatorServices.required_fields):
            raise RequiredKeyError(data, OperatorServices.required_fields)

        if not get_one(OperatorModel, id):
            raise NotFoundError

        operator = get_one(OperatorModel, id)
        update_model(operator, data)

        return get_one(OperatorModel, id)

    @staticmethod
    def delete_operator(id: int) -> None:

        if not get_one(OperatorModel, id):
            raise NotFoundError

        operator = get_one(OperatorModel, id)
        delete_commit(operator)
