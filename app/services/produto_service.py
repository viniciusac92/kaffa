from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ProdutoModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class ProdutoServices:

    required_fields = ["descricao"]

    @staticmethod
    def create_produto(data:dict):

        if verify_missing_key(data,ProdutoServices.required_fields):
            raise MissingKeyError(data, ProdutoServices.required_fields)

        if verify_recieved_keys(data, ProdutoServices.required_fields):
            raise RequiredKeyError(data, ProdutoServices.required_fields)

        produto = ProdutoModel(**data)

        add_commit(produto)
        
        return get_one(ProdutoModel, produto.id)

    @staticmethod
    def get_all_produtos():

        return get_all(ProdutoModel)

    @staticmethod
    def get_by_id(id):

        return get_one(ProdutoModel, id)

    @staticmethod
    def update_produto(data: dict, id):

        if verify_recieved_keys(data, ProdutoServices.required_fields):
            raise RequiredKeyError(data, ProdutoServices.required_fields)
        
        if not get_one(ProdutoModel, id):
            raise NotFoundError

        produto = get_one(ProdutoModel,id)
        update_model(produto, data)

        return get_one(ProdutoModel, id)

    @staticmethod
    def delete_produto(id: int) -> None:

        if not get_one(ProdutoModel, id):
            raise NotFoundError

        produto = get_one(ProdutoModel,id)
        delete_commit(produto)



