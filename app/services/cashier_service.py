from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import CashierModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)


class CashierServices:

    required_fields = ["initial_value", "balance"]

    @staticmethod
    def create_cashier(data: dict):

        if verify_missing_key(data, CashierServices.required_fields):
            raise MissingKeyError(data, CashierServices.required_fields)

        if verify_recieved_keys(data, CashierServices.required_fields):
            raise RequiredKeyError(data, CashierServices.required_fields)

        cashier = CashierModel(**data)

        add_commit(cashier)

        return get_one(CashierModel, cashier.id)

    @staticmethod
    def get_all_cashiers():

        # return get_all(CashierModel)
        cashier_list = get_all(CashierModel)
        for cashier in cashier_list:
            update_model(
                cashier, {"balance": cashier.update_balance_all_bills()})

        return cashier_list

    @staticmethod
    def get_by_id(id):

        # return get_one(CashierModel, id)
        cashier = get_one(CashierModel, id)
        update_model(cashier, {"balance": cashier.update_balance_all_bills()})

        return cashier

    @staticmethod
    def update_cashier(data: dict, id):

        if verify_recieved_keys(data, CashierServices.required_fields):
            raise RequiredKeyError(data, CashierServices.required_fields)

        if not get_one(CashierModel, id):
            raise NotFoundError

        cashier = get_one(CashierModel, id)
        update_model(cashier, data)

        return get_one(CashierModel, id)

    @staticmethod
    def delete_cashier(id: int) -> None:

        if not get_one(CashierModel, id):
            raise NotFoundError

        cashier = get_one(CashierModel, id)
        delete_commit(cashier)
