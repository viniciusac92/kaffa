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
from sqlalchemy.sql import operators

bp = Blueprint('bp_tests_v', __name__, url_prefix='/api')


@bp.route("/", methods=["GET"])
def get():
    session = db.session
    gerentes_list = (
        session.query(UserModel).join(OperatorModel).join(OperatorCashierModel).all()
    )
    # garcons_list = session.query(WaiterModel).join(UserModel).all()
    # operadores_list = session.query(OperatorModel).join(UserModel).all()
    conta_list = (
        session.query(AccountModel).join(WaiterModel).join(PaymentMethodModel).all()
    )

    # ROTA DE VENDAS

    data1 = [info for info in gerentes_list]

    data2 = [
        {
            "id": info.id,
            "data": info.date,
            "caixa": info.id_cashier,
            "garcom": info.waiter.name,
            "mesa": info.id_table,
            "forma_de_pagamento": info.payment_method.name,
        }
        for info in conta_list
    ]

    data2_2 = [info for info in conta_list]

    # example = {**data2}

    # data2 = [info.usuario.username for info in garcons_list]

    # data3 = [info.usuario.username for info in operadores_list]

    # data4 = [c.garcom_da_conta_model for info in conta_list for c in info.contas_list]

    import ipdb

    ipdb.set_trace()

    return {"msg": "teste retornou"}, HTTPStatus.OK
