from app.custom_errors import required_key
from app.custom_errors.not_found import NotFoundError

from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import CashierModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class CashierServices:

    required_fields = ["initial_value", "balance"]
    withdrawal_required_fields = ["value"]

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

        return get_all(CashierModel)


    @staticmethod
    def get_by_id(id):

        return get_one(CashierModel, id)


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


    @staticmethod
    def cash_balance(id):

        cashier: CashierModel = get_one(CashierModel, id)
        update_model(cashier, {"balance": cashier.update_balance_all_bills()})

        return cashier


    @staticmethod
    def cash_withdrawal(data: dict, id):

        if verify_missing_key(data, CashierServices.withdrawal_required_fields):
            raise MissingKeyError(data, CashierServices.withdrawal_required_fields)

        if verify_recieved_keys(data, CashierServices.withdrawal_required_fields):
            raise RequiredKeyError(data, CashierServices.withdrawal_required_fields)

        cashier: CashierModel = get_one(CashierModel, id)
        cashier.remove_from_balance(value=data["value"])
        update_model(cashier, {"balance": cashier.balance})

        return cashier