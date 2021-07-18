from http import HTTPStatus

from app.configs.database import db
from app.models import (
    AccountModel,
    AccountProductModel,
    ProductModel,
    ProviderModel,
    PurchaseOrderModel,
    WaiterModel,
)
from app.models.manager_model import ManagerModel
from app.models.product_purchase_order_model import ProductPurchaseOrderModel
from app.services.helper import create_sales_report
from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

bp = Blueprint('bp_report_purchase_order', __name__, url_prefix='/api')


@bp.route("/report_purchase_order", methods=["GET"])
# @jwt_required()
def create():
    # if get_jwt_identity()["type"] != 1:
    #     return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    session = db.session

    account_list = (
        session.query(
            PurchaseOrderModel.id,
            ProviderModel.trading_name,
            ProviderModel.cnpj,
            ManagerModel.name,
        )
        .join(PurchaseOrderModel, PurchaseOrderModel.id_provider == ProviderModel.id)
        # .join(ManagerModel, ManagerModel.id == PurchaseOrderModel.id_manager)
        .join(
            ProductPurchaseOrderModel,
            ProductPurchaseOrderModel.id_order == PurchaseOrderModel.id,
        )
        .all()
    )

    import ipdb

    ipdb.set_trace()

    if len(account_list) == 0:
        return {"message": "No open accounts"}, HTTPStatus.OK

    create_sales_report(account_list)

    return {"message": "Csv file created"}, HTTPStatus.OK
