from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import StockProductModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)


class StockProductServices:

    required_fields = ["id_product", "quantity"]

    @staticmethod
    def create_stock_product(data: dict):

        if verify_missing_key(data, StockProductServices.required_fields):
            raise MissingKeyError(data, StockProductServices.required_fields)

        if verify_recieved_keys(data, StockProductServices.required_fields):
            raise RequiredKeyError(data, StockProductServices.required_fields)

        stock_product = StockProductModel(**data)

        add_commit(stock_product)

        return get_one(StockProductModel, stock_product.id)

    @staticmethod
    def get_all_stock_products():

        return get_all(StockProductModel)

    @staticmethod
    def get_by_id(id):

        return get_one(StockProductModel, id)

    @staticmethod
    def update_stock_product(data: dict, id):

        if verify_recieved_keys(data, StockProductServices.required_fields):
            raise RequiredKeyError(data, StockProductServices.required_fields)

        if not get_one(StockProductModel, id):
            raise NotFoundError

        stock_product = get_one(StockProductModel, id)
        update_model(stock_product, data)

        return get_one(StockProductModel, id)

    @staticmethod
    def delete_stock_product(id: int) -> None:

        if not get_one(StockProductModel, id):
            raise NotFoundError

        stock_product = get_one(StockProductModel, id)
        delete_commit(stock_product)
