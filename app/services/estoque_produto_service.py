from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import EstoqueProdutoModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class EstoqueProdutoServices:

    required_fields = ["id_produto", "quantidade"]

    @staticmethod
    def create_estoque_produto(data:dict):

        if verify_missing_key(data,EstoqueProdutoServices.required_fields):
            raise MissingKeyError(data, EstoqueProdutoServices.required_fields)

        if verify_recieved_keys(data, EstoqueProdutoServices.required_fields):
            raise RequiredKeyError(data, EstoqueProdutoServices.required_fields)

        estoque_produto = EstoqueProdutoModel(**data)

        add_commit(estoque_produto)
        
        return get_one(EstoqueProdutoModel, estoque_produto.id)

    @staticmethod
    def get_all_estoque_produtos():

        return get_all(EstoqueProdutoModel)

    @staticmethod
    def get_by_id(id):

        return get_one(EstoqueProdutoModel, id)

    @staticmethod
    def update_estoque_produto(data: dict, id):

        if verify_recieved_keys(data, EstoqueProdutoServices.required_fields):
            raise RequiredKeyError(data, EstoqueProdutoServices.required_fields)
        
        if not get_one(EstoqueProdutoModel, id):
            raise NotFoundError

        estoque_produto = get_one(EstoqueProdutoModel,id)
        update_model(estoque_produto, data)

        return get_one(EstoqueProdutoModel, id)

    @staticmethod
    def delete_estoque_produto(id: int) -> None:

        if not get_one(EstoqueProdutoModel, id):
            raise NotFoundError

        estoque_produto = get_one(EstoqueProdutoModel,id)
        delete_commit(estoque_produto)



