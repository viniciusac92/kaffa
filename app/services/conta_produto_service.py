from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ContaProdutoModel, ContaModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class ContaProdutoServices:

    required_fields = ["id_conta", "id_produto", "quantity"]

    @staticmethod
    def create_conta_produto(data:dict):

        if verify_missing_key(data,ContaProdutoServices.required_fields):
            raise MissingKeyError(data, ContaProdutoServices.required_fields)

        if verify_recieved_keys(data, ContaProdutoServices.required_fields):
            raise RequiredKeyError(data, ContaProdutoServices.required_fields)

        conta_produto: ContaProdutoModel = ContaProdutoModel(**data)

        add_commit(conta_produto)
        
        return get_one(ContaProdutoModel, conta_produto.id)

    @staticmethod
    def get_all_conta_produtos():

        return get_all(ContaProdutoModel)

    @staticmethod
    def get_by_id(id):

        return get_one(ContaProdutoModel, id)

    @staticmethod
    def update_conta_produto(data: dict, id):

        if verify_recieved_keys(data, ContaProdutoServices.required_fields):
            raise RequiredKeyError(data, ContaProdutoServices.required_fields)
        
        if not get_one(ContaProdutoModel, id):
            raise NotFoundError

        conta_produto = get_one(ContaProdutoModel,id)
        update_model(conta_produto, data)

        return get_one(ContaProdutoModel, id)

    @staticmethod
    def delete_conta_produto(id: int) -> None:

        if not get_one(ContaProdutoModel, id):
            raise NotFoundError

        conta_produto = get_one(ContaProdutoModel,id)
        delete_commit(conta_produto)



