# from operator import ge
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError, FkNotFoundError
from ..models import ProviderProductModel, ProductModel, ProviderModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class ProviderProductServices:

    required_fields = ["id_product", "id_provider"]

    @staticmethod
    def create_provider_product(data: dict):

        if verify_missing_key(data, ProviderProductServices.required_fields):
            raise MissingKeyError(data, ProviderProductServices.required_fields)

        if verify_recieved_keys(data, ProviderProductServices.required_fields):
            raise RequiredKeyError(data, ProviderProductServices.required_fields)

        if not get_one(ProductModel, data["id_product"]):
            raise FkNotFoundError("id_product")

        if not get_one(ProviderModel, data["id_provider"]):
            raise FkNotFoundError("id_provider")

        provider_product = ProviderProductModel(**data)

        add_commit(provider_product)

        return get_one(ProviderProductModel, provider_product.id)

    @staticmethod
    def get_all_provider_products():

        return get_all(ProviderProductModel)

    @staticmethod
    def get_by_id(id):

        provider_product = get_one(ProviderProductModel, id)

        if not provider_product:
            raise NotFoundError

        return provider_product

    @staticmethod
    def update_provider_product(data: dict, id):

        if verify_recieved_keys(data, ProviderProductServices.required_fields):
            raise RequiredKeyError(data, ProviderProductServices.required_fields)

        if not get_one(ProviderProductModel, id):
            raise NotFoundError

        provider_product = get_one(ProviderProductModel, id)
        update_model(provider_product, data)

        return get_one(ProviderProductModel, id)

    @staticmethod
    def delete_provider_product(id: int) -> None:

        if not get_one(ProviderProductModel, id):
            raise NotFoundError

        provider_product = get_one(ProviderProductModel, id)
        delete_commit(provider_product)
