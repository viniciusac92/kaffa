from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import PurchaseOrderModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)


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

        # return get_one(PurchaseOrderModel, id)

        purchase_order: PurchaseOrderModel = get_one(PurchaseOrderModel, id)
        purchase_order.close_order()
        update_model(purchase_order, {"total_value": purchase_order.total_value})

        return purchase_order

    @staticmethod
    def update_purchase_order(data: dict, id):

        if verify_recieved_keys(data, PurchaseOrderServices.required_fields):
            raise RequiredKeyError(data, PurchaseOrderServices.required_fields)

        if not get_one(PurchaseOrderModel, id):
            raise NotFoundError

        purchase_order = get_one(PurchaseOrderModel, id)
        update_model(purchase_order, data)

        return get_one(PurchaseOrderModel, id)

    @staticmethod
    def delete_purchase_order(id: int) -> None:

        if not get_one(PurchaseOrderModel, id):
            raise NotFoundError

        purchase_order = get_one(PurchaseOrderModel, id)
        delete_commit(purchase_order)
