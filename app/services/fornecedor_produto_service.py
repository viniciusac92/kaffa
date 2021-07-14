from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import FornecedorProdutoModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class FornecedorProdutoServices:

    required_fields = ["id_produto", "id_fornecedor"]

    @staticmethod
    def create_fornecedor_produto(data:dict):

        if verify_missing_key(data,FornecedorProdutoServices.required_fields):
            raise MissingKeyError(data, FornecedorProdutoServices.required_fields)

        if verify_recieved_keys(data, FornecedorProdutoServices.required_fields):
            raise RequiredKeyError(data, FornecedorProdutoServices.required_fields)

        fornecedor_produto = FornecedorProdutoModel(**data)

        add_commit(fornecedor_produto)
        
        return get_one(FornecedorProdutoModel, fornecedor_produto.id)

    @staticmethod
    def get_all_fornecedor_produtos():

        return get_all(FornecedorProdutoModel)

    @staticmethod
    def get_by_id(id):

        return get_one(FornecedorProdutoModel, id)

    @staticmethod
    def update_fornecedor_produto(data: dict, id):

        if verify_recieved_keys(data, FornecedorProdutoServices.required_fields):
            raise RequiredKeyError(data, FornecedorProdutoServices.required_fields)
        
        if not get_one(FornecedorProdutoModel, id):
            raise NotFoundError

        fornecedor_produto = get_one(FornecedorProdutoModel,id)
        update_model(fornecedor_produto, data)

        return get_one(FornecedorProdutoModel, id)

    @staticmethod
    def delete_fornecedor_produto(id: int) -> None:

        if not get_one(FornecedorProdutoModel, id):
            raise NotFoundError

        fornecedor_produto = get_one(FornecedorProdutoModel,id)
        delete_commit(fornecedor_produto)



