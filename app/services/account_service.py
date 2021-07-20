from sqlalchemy import and_

from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError, FkNotFoundError
from ..models import AccountModel, AccountProductModel, PaymentMethodModel, WaiterModel, CashierModel, TableModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)

import ipdb

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

        if not get_one(CashierModel, data["id_cashier"]):
            raise FkNotFoundError("id_cashier")

        if not get_one(WaiterModel, data["id_waiter"]):
            raise FkNotFoundError("id_waiter")

        if not get_one(TableModel, data["id_table"]):
            raise FkNotFoundError("id_table")

        if not get_one(PaymentMethodModel, data["id_payment_method"]):
            raise FkNotFoundError("id_payment_method")

        account = AccountModel(**data)

        add_commit(account)

        bill = get_one(AccountModel, account.id)

        return {
            "id": bill.id,
            "date": bill.date,
            "id_cashier": bill.id_cashier,
            "waiter": WaiterModel.query.get(bill.id_waiter).name,
            "id_table": bill.id_table,
            "payment_method": PaymentMethodModel.query.get(bill.id_payment_method).name,
            "status": bill.status,
            "total_value": bill.total_value,
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
                    "subtotal": product.price * AccountProductModel.query.filter(
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
                "status": bill.status,
                "total_value": bill.total_value,
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
                        "subtotal": product.price * AccountProductModel.query.filter(
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

        if not bill:
            raise NotFoundError

        return {
            "id": bill.id,
            "date": bill.date,
            "id_cashier": bill.id_cashier,
            "waiter": WaiterModel.query.get(bill.id_waiter).name,
            "id_table": bill.id_table,
            "payment_method": PaymentMethodModel.query.get(bill.id_payment_method).name,
            "status": bill.status,
            "total_value": bill.total_value,
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
                    "subtotal": product.price * AccountProductModel.query.filter(
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

        bill = get_one(AccountModel, id)
        update_model(bill, data)

        return {
            "id": bill.id,
            "data": bill.data,
            "id_cashier": bill.id_cashier,
            "waiter": WaiterModel.query.get(bill.id_waiter).name,
            "id_table": bill.id_table,
            "payment_method": PaymentMethodModel.query.get(bill.id_payment_method).name,
            "status": bill.status,
            "total_value": bill.total_value,
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
                    "subtotal": product.price * AccountProductModel.query.filter(
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

    @staticmethod
    def close_account(id):

        bill: AccountModel = get_one(AccountModel, id)

        if not bill:
            raise NotFoundError

        bill.close_bill()
        update_model(bill, {"is_finished": True})

        return {
            "id": bill.id,
            "date": bill.date,
            "id_cashier": bill.id_cashier,
            "waiter": WaiterModel.query.get(bill.id_waiter).name,
            "id_table": bill.id_table,
            "payment_method": PaymentMethodModel.query.get(bill.id_payment_method).name,
            "status": bill.status,
            "total_value": bill.total_value,
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
                    "subtotal": product.price * AccountProductModel.query.filter(
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