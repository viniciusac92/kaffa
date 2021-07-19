from sqlalchemy import and_
from app.models.product_model import ProductModel
from app.custom_errors import required_key
from app.custom_errors.not_found import NotFoundError

from ..custom_errors import MissingKeyError, RequiredKeyError, PurchaseClosedError
from ..models import PurchaseOrderModel, ProductPurchaseOrderModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class PurchaseOrderServices:

    required_fields = ["id_manager", "id_provider", "date"]

    @staticmethod
    def create_purchase_order(data: dict):

        if verify_missing_key(data, PurchaseOrderServices.required_fields):
            raise MissingKeyError(data, PurchaseOrderServices.required_fields)

        if verify_recieved_keys(data, PurchaseOrderServices.required_fields):
            raise RequiredKeyError(data, PurchaseOrderServices.required_fields)

        purchase_order = PurchaseOrderModel(**data)

        add_commit(purchase_order)

        return get_one(PurchaseOrderModel, purchase_order.id)

    @staticmethod
    def get_all_purchase_orders():

        return get_all(PurchaseOrderModel)

    @staticmethod
    def get_by_id(id):

        return get_one(PurchaseOrderModel, id)

        # purchase_order: PurchaseOrderModel = get_one(PurchaseOrderModel, id)
        # purchase_order.close_order()
        # update_model(purchase_order, {"total_value": purchase_order.total_value})

        # return purchase_order

    @staticmethod
    def update_purchase_order(data: dict, id):

        if verify_recieved_keys(data, PurchaseOrderServices.required_fields):
            raise RequiredKeyError(data, PurchaseOrderServices.required_fields)

        if not get_one(PurchaseOrderModel, id):
            raise NotFoundError

        purchase_order: PurchaseOrderModel = get_one(PurchaseOrderModel, id)
        if purchase_order.is_finished:
            raise PurchaseClosedError()

        update_model(purchase_order, data)

        return get_one(PurchaseOrderModel, id)

    @staticmethod
    def delete_purchase_order(id: int) -> None:

        if not get_one(PurchaseOrderModel, id):
            raise NotFoundError

        purchase_order = get_one(PurchaseOrderModel, id)
        delete_commit(purchase_order)

    @staticmethod
    def close_purchase_order(id):
        purchase_order: PurchaseOrderModel = get_one(PurchaseOrderModel, id)
        purchase_order.close_order()
        update_model(purchase_order, {"total_value": purchase_order.total_value})

        return {
            "id": purchase_order.id,
            "date": purchase_order.date,
            "id_manager": purchase_order.id_manager,
            "id_provider": purchase_order.id_provider,
            "is_finished": purchase_order.is_finished,
            "total_value": purchase_order.total_value,
            "products_list": [
                {
                    "id": product.id,
                    "name": product.name,
                    "quantity": ProductPurchaseOrderModel.query.filter(and_(ProductPurchaseOrderModel.id_order == purchase_order.id, ProductPurchaseOrderModel.id_product == product.id)).first().quantity,
                    "cost": ProductPurchaseOrderModel.query.filter(and_(ProductPurchaseOrderModel.id_order == purchase_order.id, ProductPurchaseOrderModel.id_product == product.id)).first().cost,
                    "subtotal": ProductPurchaseOrderModel.query.filter(and_(ProductPurchaseOrderModel.id_order == purchase_order.id, ProductPurchaseOrderModel.id_product == product.id)).first().quantity * ProductPurchaseOrderModel.query.filter(and_(ProductPurchaseOrderModel.id_order == purchase_order.id, ProductPurchaseOrderModel.id_product == product.id)).first().cost
                }
                for product in purchase_order.products_list
            ]

        }