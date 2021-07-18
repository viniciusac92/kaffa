from http import HTTPStatus

from app.configs.database import db
from app.models import AccountModel, AccountProductModel, ProductModel, WaiterModel
from app.services.helper import create_sales_report
from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

bp = Blueprint('bp_sales_report', __name__, url_prefix='/api')


@bp.route("/sales_report", methods=["GET"])
# @jwt_required()
def create():
    # if get_jwt_identity()["type"] != 1:
    #     return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    session = db.session

    account_list = (
        session.query(
            WaiterModel.id,
            WaiterModel.name,
            AccountModel.id,
            AccountModel.is_finished,
            ProductModel.name,
            ProductModel.price,
            AccountProductModel.quantity,
            ProductModel.price * AccountProductModel.quantity,
        )
        .join(AccountModel, AccountModel.id_waiter == WaiterModel.id)
        .join(AccountProductModel, AccountProductModel.id_account == AccountModel.id)
        .join(ProductModel, ProductModel.id == AccountProductModel.id_product)
        .filter(AccountModel.is_finished == False)
        .all()
    )

    if len(account_list) == 0:
        return {"message": "No open accounts"}, HTTPStatus.OK

    # data2_2 = [info for info in account_list]

    create_sales_report(account_list)

    # import ipdb

    # ipdb.set_trace()

    return {"message": "Csv file created"}, HTTPStatus.OK
