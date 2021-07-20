from app.custom_errors import required_key
from app.custom_errors.not_found import NotFoundError

from ..custom_errors import (
    AccountClosedError,
    MissingKeyError,
    OutOfStockError,
    RequiredKeyError,
    FkNotFoundError
)
from ..models import AccountModel, AccountProductModel, ProductModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class AccountProductServices:

    required_fields = ["id_account", "id_product", "quantity"]

    @staticmethod
    def create_account_product(data: dict):

        if verify_missing_key(data, AccountProductServices.required_fields):
            raise MissingKeyError(data, AccountProductServices.required_fields)

        if verify_recieved_keys(data, AccountProductServices.required_fields):
            raise RequiredKeyError(data, AccountProductServices.required_fields)

        if not get_one(AccountModel, data["id_account"]):
            raise FkNotFoundError("id_account")

        if not get_one(ProductModel, data["id_product"]):
            raise FkNotFoundError("id_product")

        product: ProductModel = ProductModel.query.get(data["id_product"])
        if data["quantity"] > product.stock:
            raise OutOfStockError(product.name)

        account: AccountModel = AccountModel.query.get(data["id_account"])
        if account.status != "opened":
            raise AccountClosedError()

        account_product: AccountProductModel = AccountProductModel(**data)

        add_commit(account_product)

        return get_one(AccountProductModel, account_product.id)

    @staticmethod
    def get_all_account_products():

        return get_all(AccountProductModel)

    @staticmethod
    def get_by_id(id):

        account_product = get_one(AccountProductModel, id)

        if not account_product:
            raise NotFoundError

        return account_product

    @staticmethod
    def update_account_product(data: dict, id):

        if verify_recieved_keys(data, AccountProductServices.required_fields):
            raise RequiredKeyError(data, AccountProductServices.required_fields)

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
