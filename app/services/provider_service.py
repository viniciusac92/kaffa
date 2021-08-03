from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError, UniqueKeyError
from ..models import ProviderModel
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


class ProviderServices:

    required_fields = ["trading_name", "cnpj", "phone"]
    unique_keys = ["cnpj", "phone"]

    @staticmethod
    def create_provider(data: dict):

        if verify_missing_key(data, ProviderServices.required_fields):
            raise MissingKeyError(data, ProviderServices.required_fields)

        if verify_recieved_keys(data, ProviderServices.required_fields):
            raise RequiredKeyError(data, ProviderServices.required_fields)

        if verify_unique_keys(data, ProviderModel, ProviderServices.unique_keys):
            raise UniqueKeyError(ProviderServices.unique_keys)

        provider = ProviderModel(**data)

        add_commit(provider)

        return get_one(ProviderModel, provider.id)

    @staticmethod
    def get_all_providers():

        return get_all(ProviderModel)

    @staticmethod
    def get_by_id(id):

        provider = get_one(ProviderModel, id)

        if not provider:
            raise NotFoundError

        return provider

    @staticmethod
    def update_provider(data: dict, id):

        if verify_recieved_keys(data, ProviderServices.required_fields):
            raise RequiredKeyError(data, ProviderServices.required_fields)

        if not get_one(ProviderModel, id):
            raise NotFoundError

        provider = get_one(ProviderModel, id)
        update_model(provider, data)

        return get_one(ProviderModel, id)

    @staticmethod
    def delete_provider(id: int) -> None:

        if not get_one(ProviderModel, id):
            raise NotFoundError

        provider = get_one(ProviderModel, id)
        delete_commit(provider)
