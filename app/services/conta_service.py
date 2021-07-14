from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ContaModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class ContaServices:

    required_fields = ["data", "id_caixa", "id_garcom", "id_mesa", "id_forma_pagamento"]

    @staticmethod
    def create_conta(data:dict):

        if verify_missing_key(data,ContaServices.required_fields):
            raise MissingKeyError(data, ContaServices.required_fields)

        if verify_recieved_keys(data, ContaServices.required_fields):
            raise RequiredKeyError(data, ContaServices.required_fields)

        conta = ContaModel(**data)

        add_commit(conta)
        
        return get_one(ContaModel, conta.id)

    @staticmethod
    def get_all_contas():

        return get_all(ContaModel)

    
    @staticmethod
    def get_by_id(id):

        # return get_one(ContaModel, id)
        conta: ContaModel = get_one(ContaModel, id)
        valor_conta = conta.atualizar_valor_conta()
        print(valor_conta)
        return conta


    @staticmethod
    def update_conta(data: dict, id):

        if verify_recieved_keys(data, ContaServices.required_fields):
            raise RequiredKeyError(data, ContaServices.required_fields)
        
        if not get_one(ContaModel, id):
            raise NotFoundError

        usuario = get_one(ContaModel,id)
        update_model(usuario, data)

        return get_one(ContaModel, id)

    @staticmethod
    def delete_conta(id: int) -> None:

        if not get_one(ContaModel, id):
            raise NotFoundError

        usuario = get_one(ContaModel,id)
        delete_commit(usuario)

    @staticmethod
    def found_conta(username):
        return ContaModel.query.filter_by(username=username).first()
