from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ProductPurchaseOrderModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)


class ProductPurchaseOrderServices:

    required_fields = ["id_order", "id_product"]

    @staticmethod
    def create_product_purchase_order(data: dict):

        if verify_missing_key(data, ProductPurchaseOrderServices.required_fields):
            raise MissingKeyError(
                data, ProductPurchaseOrderServices.required_fields)

        if verify_recieved_keys(data, ProductPurchaseOrderServices.required_fields):
            raise RequiredKeyError(
                data, ProductPurchaseOrderServices.required_fields)

        product_purchase_order = ProductPurchaseOrderModel(**data)

        add_commit(product_purchase_order)

        return get_one(ProductPurchaseOrderModel, product_purchase_order.id)

    @staticmethod
    def get_all_product_purchase_orders():

        return get_all(ProductPurchaseOrderModel)

    @staticmethod
    def get_by_id(id):

        return get_one(ProductPurchaseOrderModel, id)

    @staticmethod
    def update_product_purchase_order(data: dict, id):

        if verify_recieved_keys(data, ProductPurchaseOrderServices.required_fields):
            raise RequiredKeyError(
                data, ProductPurchaseOrderServices.required_fields)

        if not get_one(ProductPurchaseOrderModel, id):
            raise NotFoundError

        product_purchase_order = get_one(ProductPurchaseOrderModel, id)
        update_model(product_purchase_order, data)

        return get_one(ProductPurchaseOrderModel, id)

    @staticmethod
    def delete_product_purchase_order(id: int) -> None:

        if not get_one(ProductPurchaseOrderModel, id):
            raise NotFoundError

        product_purchase_order = get_one(ProductPurchaseOrderModel, id)
        delete_commit(product_purchase_order)
