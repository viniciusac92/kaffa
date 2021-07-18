from app.custom_errors import required_key
from app.custom_errors.not_found import NotFoundError

from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import OperatorCashierModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class OperatorCashierServices:

    required_fields = ["id_operator", "id_cashier", "date"]

    @staticmethod
    def create_operator_cashier(data: dict):

        if verify_missing_key(data, OperatorCashierServices.required_fields):
            raise MissingKeyError(data, OperatorCashierServices.required_fields)

        if verify_recieved_keys(data, OperatorCashierServices.required_fields):
            raise RequiredKeyError(data, OperatorCashierServices.required_fields)

        operator_cashier = OperatorCashierModel(**data)

        add_commit(operator_cashier)

        return get_one(OperatorCashierModel, operator_cashier.id)

    @staticmethod
    def get_all_operator_cashiers():

        return get_all(OperatorCashierModel)

    @staticmethod
    def get_by_id(id):

        return get_one(OperatorCashierModel, id)

    @staticmethod
    def update_operator_cashier(data: dict, id):

        if verify_recieved_keys(data, OperatorCashierServices.required_fields):
            raise RequiredKeyError(data, OperatorCashierServices.required_fields)

        if not get_one(OperatorCashierModel, id):
            raise NotFoundError

        operator_cashier = get_one(OperatorCashierModel, id)
        update_model(operator_cashier, data)

        return get_one(OperatorCashierModel, id)

    @staticmethod
    def delete_operator_cashier(id: int) -> None:

        if not get_one(OperatorCashierModel, id):
            raise NotFoundError

        operator_cashier = get_one(OperatorCashierModel, id)
        delete_commit(operator_cashier)
