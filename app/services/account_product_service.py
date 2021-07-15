from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import AccountProductModel, AccountModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)


class AccountProductServices:

    required_fields = ["id_account", "id_product", "quantity"]

    @staticmethod
    def create_account_product(data: dict):

        if verify_missing_key(data, AccountProductServices.required_fields):
            raise MissingKeyError(data, AccountProductServices.required_fields)

        if verify_recieved_keys(data, AccountProductServices.required_fields):
            raise RequiredKeyError(
                data, AccountProductServices.required_fields)

        account_product: AccountProductModel = AccountProductModel(**data)

        add_commit(account_product)

        return get_one(AccountProductModel, account_product.id)

    @staticmethod
    def get_all_account_products():

        return get_all(AccountProductModel)

    @staticmethod
    def get_by_id(id):

        return get_one(AccountProductModel, id)

    @staticmethod
    def update_account_product(data: dict, id):

        if verify_recieved_keys(data, AccountProductServices.required_fields):
            raise RequiredKeyError(
                data, AccountProductServices.required_fields)

        if not get_one(AccountProductModel, id):
            raise NotFoundError

        account_product = get_one(AccountProductModel, id)
        update_model(account_product, data)

        return get_one(AccountProductModel, id)

    @staticmethod
    def delete_account_product(id: int) -> None:

        if not get_one(AccountProductModel, id):
            raise NotFoundError

        account_product = get_one(AccountProductModel, id)
        delete_commit(account_product)
