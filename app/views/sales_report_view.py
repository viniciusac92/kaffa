from http import HTTPStatus

from app.configs.database import db
from app.models import (
    AccountModel,
    AccountProductModel,
    ManagerModel,
    OperatorCashierModel,
    OperatorModel,
    PaymentMethodModel,
    ProductModel,
    UserModel,
    WaiterModel,
)
from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.sql import operators

bp = Blueprint('bp_sales_report', __name__, url_prefix='/api')


@bp.route("/sales_report", methods=["GET"])
# @jwt_required()
def create():
    # if get_jwt_identity()["type"] != 1:
    #     return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    session = db.session

    account_list = (
        session.query(
            WaiterModel.name,
            AccountModel.id,
            ProductModel.name,
            ProductModel.price * AccountProductModel.quantity,
        )
        .join(AccountModel, AccountModel.id_waiter == WaiterModel.id)
        .join(AccountProductModel, AccountProductModel.id_account == AccountModel.id)
        .join(ProductModel, ProductModel.id == AccountProductModel.id_product)
        .all()
    )

    # data2 = [
    #     {
    #         "id": info.id,
    #         "data": info.date,
    #         "caixa": info.id_cashier,
    #         "garcom": info.waiter.name,
    #         "mesa": info.id_table,
    #         "forma_de_pagamento": info.payment_method.name,
    #     }
    #     for info in account_list
    # ]

    data2_2 = [info for info in account_list]

    import ipdb

    ipdb.set_trace()

    return {"message": "Csv file created"}, HTTPStatus.OK
