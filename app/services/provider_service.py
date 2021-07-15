from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ProviderModel
from . import (add_commit, get_all, get_one, verify_recieved_keys,
               update_model, delete_commit, verify_missing_key)


class ProviderServices:

    required_fields = ["trading_name", "cnpj", "phone"]

    @staticmethod
    def create_provider(data: dict):

        if verify_missing_key(data, ProviderServices.required_fields):
            raise MissingKeyError(data, ProviderServices.required_fields)

        if verify_recieved_keys(data, ProviderServices.required_fields):
            raise RequiredKeyError(data, ProviderServices.required_fields)

        provider = ProviderModel(**data)

        add_commit(provider)

        return get_one(ProviderModel, provider.id)

    @staticmethod
    def get_all_providers():

        return get_all(ProviderModel)

    @staticmethod
    def get_by_id(id):

        return get_one(ProviderModel, id)

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
