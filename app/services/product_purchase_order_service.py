from ..custom_errors import MissingKeyError, RequiredKeyError, PurchaseClosedError, FkNotFoundError, NotFoundError
from ..models import ProductPurchaseOrderModel, PurchaseOrderModel, ProductModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class ProductPurchaseOrderServices:

    required_fields = ["id_order", "id_product", "quantity", "cost"]

    @staticmethod
    def create_product_purchase_order(data: dict):

        if verify_missing_key(data, ProductPurchaseOrderServices.required_fields):
            raise MissingKeyError(data, ProductPurchaseOrderServices.required_fields)

        if verify_recieved_keys(data, ProductPurchaseOrderServices.required_fields):
            raise RequiredKeyError(data, ProductPurchaseOrderServices.required_fields)

        if not get_one(PurchaseOrderModel, data["id_order"]):
            raise FkNotFoundError("id_order")

        if not get_one(ProductModel, data["id_product"]):
            raise FkNotFoundError("id_product")

        purchase_order: PurchaseOrderModel = PurchaseOrderModel.query.get(
            data["id_order"]
        )
        if purchase_order.is_finished:
            raise PurchaseClosedError()

        product_purchase_order = ProductPurchaseOrderModel(**data)

        add_commit(product_purchase_order)

        return get_one(ProductPurchaseOrderModel, product_purchase_order.id)

    @staticmethod
    def get_all_product_purchase_orders():

        return get_all(ProductPurchaseOrderModel)

    @staticmethod
    def get_by_id(id):

        product_purchase_order = get_one(ProductPurchaseOrderModel, id)

        if not product_purchase_order:
            raise NotFoundError

        return product_purchase_order

    @staticmethod
    def update_product_purchase_order(data: dict, id):

        if verify_recieved_keys(data, ProductPurchaseOrderServices.required_fields):
            raise RequiredKeyError(data, ProductPurchaseOrderServices.required_fields)

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
