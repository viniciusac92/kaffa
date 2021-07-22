from ..custom_errors import (
    MissingKeyError,
    NotFoundError,
    RequiredKeyError,
    UniqueKeyError,
)
from ..models import ProductModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
    verify_unique_keys,
)


class ProductServices:

    required_fields = ["name", "description", "price", "stock"]
    unique_keys = ["name"]

    @staticmethod
    def create_product(data: dict):

        if verify_missing_key(data, ProductServices.required_fields):
            raise MissingKeyError(data, ProductServices.required_fields)

        if verify_recieved_keys(data, ProductServices.required_fields):
            raise RequiredKeyError(data, ProductServices.required_fields)

        if verify_unique_keys(data, ProductModel, ProductServices.unique_keys):
            raise UniqueKeyError(ProductServices.unique_keys)

        product = ProductModel(**data)

        add_commit(product)

        return get_one(ProductModel, product.id)

    @staticmethod
    def get_all_products():

        return get_all(ProductModel)

    @staticmethod
    def get_by_id(id):

        product = get_one(ProductModel, id)

        if not product:
            raise NotFoundError

        return product

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
