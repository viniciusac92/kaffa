from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ProdutoOrdemDeCompraModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class ProdutoOrdemCompraServices:

    required_fields = ["id_ordem", "id_produto"]

    @staticmethod
    def create_produto_ordem_compra(data:dict):

        if verify_missing_key(data,ProdutoOrdemCompraServices.required_fields):
            raise MissingKeyError(data, ProdutoOrdemCompraServices.required_fields)

        if verify_recieved_keys(data, ProdutoOrdemCompraServices.required_fields):
            raise RequiredKeyError(data, ProdutoOrdemCompraServices.required_fields)

        produto_ordem_compra = ProdutoOrdemDeCompraModel(**data)

        add_commit(produto_ordem_compra)
        
        return get_one(ProdutoOrdemDeCompraModel, produto_ordem_compra.id)

    @staticmethod
    def get_all_produto_ordem_compras():

        return get_all(ProdutoOrdemDeCompraModel)

    @staticmethod
    def get_by_id(id):

        return get_one(ProdutoOrdemDeCompraModel, id)

    @staticmethod
    def update_produto_ordem_compra(data: dict, id):

        if verify_recieved_keys(data, ProdutoOrdemCompraServices.required_fields):
            raise RequiredKeyError(data, ProdutoOrdemCompraServices.required_fields)
        
        if not get_one(ProdutoOrdemDeCompraModel, id):
            raise NotFoundError

        produto_ordem_compra = get_one(ProdutoOrdemDeCompraModel,id)
        update_model(produto_ordem_compra, data)

        return get_one(ProdutoOrdemDeCompraModel, id)

    @staticmethod
    def delete_produto_ordem_compra(id: int) -> None:

        if not get_one(ProdutoOrdemDeCompraModel, id):
            raise NotFoundError

        produto_ordem_compra = get_one(ProdutoOrdemDeCompraModel,id)
        delete_commit(produto_ordem_compra)



