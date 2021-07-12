from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import OrdemDeCompraModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class OrdemCompraServices:

    required_fields = ["id_fornecedor", "data"]

    @staticmethod
    def create_ordem_compra(data:dict):

        if verify_missing_key(data,OrdemCompraServices.required_fields):
            raise MissingKeyError(data, OrdemCompraServices.required_fields)

        if verify_recieved_keys(data, OrdemCompraServices.required_fields):
            raise RequiredKeyError(data, OrdemCompraServices.required_fields)

        ordem_compra = OrdemDeCompraModel(**data)

        add_commit(ordem_compra)
        
        return get_one(OrdemDeCompraModel, ordem_compra.id)

    @staticmethod
    def get_all_ordem_compras():

        return get_all(OrdemDeCompraModel)

    @staticmethod
    def get_by_id(id):

        return get_one(OrdemDeCompraModel, id)

    @staticmethod
    def update_ordem_compra(data: dict, id):

        if verify_recieved_keys(data, OrdemCompraServices.required_fields):
            raise RequiredKeyError(data, OrdemCompraServices.required_fields)
        
        if not get_one(OrdemDeCompraModel, id):
            raise NotFoundError

        ordem_compra = get_one(OrdemDeCompraModel,id)
        update_model(ordem_compra, data)

        return get_one(OrdemDeCompraModel, id)

    @staticmethod
    def delete_ordem_compra(id: int) -> None:

        if not get_one(OrdemDeCompraModel, id):
            raise NotFoundError

        ordem_compra = get_one(OrdemDeCompraModel,id)
        delete_commit(ordem_compra)



