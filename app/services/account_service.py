from app.custom_errors import required_key
from app.custom_errors.not_found import NotFoundError
from sqlalchemy import and_

from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import AccountModel, AccountProductModel, PaymentMethodModel, WaiterModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class AccountServices:

    required_fields = [
        "date",
        "id_cashier",
        "id_waiter",
        "id_table",
        "id_payment_method",
    ]

    @staticmethod
    def create_account(data: dict):

        if verify_missing_key(data, AccountServices.required_fields):
            raise MissingKeyError(data, AccountServices.required_fields)

        if verify_recieved_keys(data, AccountServices.required_fields):
            raise RequiredKeyError(data, AccountServices.required_fields)

        account = AccountModel(**data)

        add_commit(account)

        # return get_one(AccountModel, account.id)

        bill = get_one(AccountModel, account.id)

        return {
            "id": bill.id,
            "date": bill.date,
            "id_cashier": bill.id_cashier,
            "waiter": WaiterModel.query.get(bill.id_waiter).name,
            "id_table": bill.id_table,
            "payment_method": PaymentMethodModel.query.get(bill.id_payment_method).name,
            "is_finished": bill.is_finished,
            "product_list": [
                {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "quantity": AccountProductModel.query.filter(
                        and_(
                            AccountProductModel.id_product == product.id,
                            AccountProductModel.id_account == bill.id,
                        )
                    )
                    .first()
                    .quantity,
                }
                for product in bill.product_list
            ],
        }

    @staticmethod
    def get_all_accounts():

        bill_list = get_all(AccountModel)

        return [
            {
                "id": bill.id,
                "date": bill.date,
                "id_cashier": bill.id_cashier,
                "waiter": WaiterModel.query.get(bill.id_waiter).name,
                "id_table": bill.id_table,
                "payment_method": PaymentMethodModel.query.get(
                    bill.id_payment_method
                ).name,
                "is_finished": bill.is_finished,
                "product_list": [
                    {
                        "id": product.id,
                        "name": product.name,
                        "description": product.description,
                        "price": product.price,
                        "quantity": AccountProductModel.query.filter(
                            and_(
                                AccountProductModel.id_product == product.id,
                                AccountProductModel.id_account == bill.id,
                            )
                        )
                        .first()
                        .quantity,
                    }
                    for product in bill.product_list
                ],
            }
            for bill in bill_list
        ]

    @staticmethod
    def get_by_id(id):

        bill = get_one(AccountModel, id)

        return {
            "id": bill.id,
            "date": bill.date,
            "id_cashier": bill.id_cashier,
            "waiter": WaiterModel.query.get(bill.id_waiter).name,
            "id_table": bill.id_table,
            "payment_method": PaymentMethodModel.query.get(bill.id_payment_method).name,
            "is_finished": bill.is_finished,
            "product_list": [
                {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "quantity": AccountProductModel.query.filter(
                        and_(
                            AccountProductModel.id_product == product.id,
                            AccountProductModel.id_account == bill.id,
                        )
                    )
                    .first()
                    .quantity,
                }
                for product in bill.product_list
            ],
        }

    @staticmethod
    def update_account(data: dict, id):

        if verify_recieved_keys(data, AccountServices.required_fields):
            raise RequiredKeyError(data, AccountServices.required_fields)

        if not get_one(AccountModel, id):
            raise NotFoundError

        user = get_one(AccountModel, id)
        update_model(user, data)

        # return get_one(AccountModel, id)
        bill = get_one(AccountModel, id)

        return {
            "id": bill.id,
            "data": bill.data,
            "id_cashier": bill.id_cashier,
            "waiter": WaiterModel.query.get(bill.id_waiter).name,
            "id_table": bill.id_table,
            "payment_method": PaymentMethodModel.query.get(bill.id_payment_method).name,
            "is_finished": bill.is_finished,
            "product_list": [
                {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "quantity": AccountProductModel.query.filter(
                        and_(
                            AccountProductModel.id_product == product.id,
                            AccountProductModel.id_account == bill.id,
                        )
                    )
                    .first()
                    .quantity,
                }
                for product in bill.product_list
            ],
        }

    @staticmethod
    def delete_account(id: int) -> None:

        if not get_one(AccountModel, id):
            raise NotFoundError

        user = get_one(AccountModel, id)
        delete_commit(user)

    @staticmethod
    def found_account(username):
        return AccountModel.query.filter_by(username=username).first()
