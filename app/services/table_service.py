from app.custom_errors import required_key
from app.custom_errors.not_found import NotFoundError

from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import TableModel
from .helper import (
    add_commit,
    delete_commit,
    get_all,
    get_one,
    update_model,
    verify_missing_key,
    verify_recieved_keys,
)


class TableServices:

    required_fields = ["number"]

    @staticmethod
    def create_table(data: dict):

        if verify_missing_key(data, TableServices.required_fields):
            raise MissingKeyError(data, TableServices.required_fields)

        if verify_recieved_keys(data, TableServices.required_fields):
            raise RequiredKeyError(data, TableServices.required_fields)

        table = TableModel(**data)

        add_commit(table)

        return get_one(TableModel, table.id)

    @staticmethod
    def get_all_tables():

        return get_all(TableModel)

    @staticmethod
    def get_by_id(id):

        return get_one(TableModel, id)

    @staticmethod
    def update_table(data: dict, id):

        if verify_recieved_keys(data, TableServices.required_fields):
            raise RequiredKeyError(data, TableServices.required_fields)

        if not get_one(TableModel, id):
            raise NotFoundError

        table = get_one(TableModel, id)
        update_model(table, data)

        return get_one(TableModel, id)

    @staticmethod
    def delete_table(id: int) -> None:

        if not get_one(TableModel, id):
            raise NotFoundError

        table = get_one(TableModel, id)
        delete_commit(table)
