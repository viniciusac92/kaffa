from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ProductModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)


class ProductServices:

    required_fields = ["name", "description", "price", "stock"]

    @staticmethod
    def create_product(data: dict):

        if verify_missing_key(data, ProductServices.required_fields):
            raise MissingKeyError(data, ProductServices.required_fields)

        if verify_recieved_keys(data, ProductServices.required_fields):
            raise RequiredKeyError(data, ProductServices.required_fields)

        product = ProductModel(**data)

        add_commit(product)

        return get_one(ProductModel, product.id)

    @staticmethod
    def get_all_products():

        return get_all(ProductModel)

    @staticmethod
    def get_by_id(id):

        return get_one(ProductModel, id)

    @staticmethod
    def update_product(data: dict, id):

        if verify_recieved_keys(data, ProductServices.required_fields):
            raise RequiredKeyError(data, ProductServices.required_fields)

        if not get_one(ProductModel, id):
            raise NotFoundError

        product = get_one(ProductModel, id)
        update_model(product, data)

        return get_one(ProductModel, id)

    @staticmethod
    def delete_product(id: int) -> None:

        if not get_one(ProductModel, id):
            raise NotFoundError

        product = get_one(ProductModel, id)
        delete_commit(product)
