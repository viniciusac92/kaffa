from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError, ImmutableAttrError
from datetime import date
from ..models import WaiterModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)

from ipdb import set_trace
class WaiterServices:

    required_fields = ["name", "cpf", "id_user"]

    @staticmethod
    def create_waiter(data: dict):

        if verify_missing_key(data, WaiterServices.required_fields):
            raise MissingKeyError(data, WaiterServices.required_fields)

        if verify_recieved_keys(data, WaiterServices.required_fields):
            raise RequiredKeyError(data, WaiterServices.required_fields)

        waiter = WaiterModel(**data)

        add_commit(waiter)

        return get_one(WaiterModel, waiter.id)

    @staticmethod
    def get_all_waiters():

        return get_all(WaiterModel)

    @staticmethod
    def get_by_id(id):

        waiter: WaiterModel = get_one(WaiterModel, id)

        if not waiter:
            raise NotFoundError

        # set_trace()

        return   {
            "id": waiter.id,
            "name": waiter.name,
            "cpf": waiter.cpf,
            "id_user": waiter.id_user,
            "account_list": [
                {
                    "id": account.id,
                    "date": account.date,
                    "status": account.status,
                    "total_value": account.total_value
                }
                for account in waiter.account_list if account.date.strftime("%m/%d/%Y") == date.today().strftime("%m/%d/%Y")
            ]
        }

    @staticmethod
    def update_waiter(data: dict, id):

        if verify_recieved_keys(data, WaiterServices.required_fields):
            raise RequiredKeyError(data, WaiterServices.required_fields)

        if not get_one(WaiterModel, id):
            raise NotFoundError

        if data.get("id_user"):
            raise ImmutableAttrError("id_user")

        waiter = get_one(WaiterModel, id)
        update_model(waiter, data)

        return get_one(WaiterModel, id)

    @staticmethod
    def delete_waiter(id: int) -> None:

        if not get_one(WaiterModel, id):
            raise NotFoundError

        waiter = get_one(WaiterModel, id)
        delete_commit(waiter)
