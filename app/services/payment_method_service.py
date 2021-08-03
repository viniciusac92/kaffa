from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError, UniqueKeyError
from ..models import PaymentMethodModel
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


class PaymentMethodServices:

    required_fields = ["name", "description"]
    unique_keys = ["name"]

    @staticmethod
    def create_payment_method(data: dict):

        if verify_missing_key(data, PaymentMethodServices.required_fields):
            raise MissingKeyError(data, PaymentMethodServices.required_fields)

        if verify_recieved_keys(data, PaymentMethodServices.required_fields):
            raise RequiredKeyError(data, PaymentMethodServices.required_fields)

        if verify_unique_keys(data, PaymentMethodModel, PaymentMethodServices.unique_keys):
            raise UniqueKeyError(PaymentMethodServices.unique_keys)

        payment_method = PaymentMethodModel(**data)

        add_commit(payment_method)

        return get_one(PaymentMethodModel, payment_method.id)

    @staticmethod
    def get_all_payment_method():

        return get_all(PaymentMethodModel)

    @staticmethod
    def get_by_id(id):

        payment_method = get_one(PaymentMethodModel, id)

        if not payment_method:
            raise NotFoundError

        return get_one(PaymentMethodModel, id)

    @staticmethod
    def update_payment_method(data: dict, id):

        if verify_recieved_keys(data, PaymentMethodServices.required_fields):
            raise RequiredKeyError(data, PaymentMethodServices.required_fields)

        if not get_one(PaymentMethodModel, id):
            raise NotFoundError

        payment_method = get_one(PaymentMethodModel, id)
        update_model(payment_method, data)

        return get_one(PaymentMethodModel, id)

    @staticmethod
    def delete_payment_method(id: int) -> None:

        if not get_one(PaymentMethodModel, id):
            raise NotFoundError

        payment_method = get_one(PaymentMethodModel, id)
        delete_commit(payment_method)
