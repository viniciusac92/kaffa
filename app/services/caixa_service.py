from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import CaixaModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

import ipdb

class CaixaServices:

    required_fields = ["valor_inicial", "saldo"]

    @staticmethod
    def create_caixa(data:dict):

        if verify_missing_key(data,CaixaServices.required_fields):
            raise MissingKeyError(data, CaixaServices.required_fields)

        if verify_recieved_keys(data, CaixaServices.required_fields):
            raise RequiredKeyError(data, CaixaServices.required_fields)

        caixa = CaixaModel(**data)

        add_commit(caixa)
        
        return get_one(CaixaModel, caixa.id)

    @staticmethod
    def get_all_caixas():

        # return get_all(CaixaModel)
        caixa_list = get_all(CaixaModel)
        for caixa in caixa_list:
            update_model(caixa, {"saldo": caixa.update_balance_all_bills() })
        
        return caixa_list

    @staticmethod
    def get_by_id(id):

        # return get_one(CaixaModel, id)
        caixa = get_one(CaixaModel, id)

        update_model(caixa, {"saldo": caixa.update_balance_all_bills() })
        
        return caixa



    @staticmethod
    def update_caixa(data: dict, id):

        if verify_recieved_keys(data, CaixaServices.required_fields):
            raise RequiredKeyError(data, CaixaServices.required_fields)
        
        if not get_one(CaixaModel, id):
            raise NotFoundError

        caixa = get_one(CaixaModel,id)
        update_model(caixa, data)

        return get_one(CaixaModel, id)

    @staticmethod
    def delete_caixa(id: int) -> None:

        if not get_one(CaixaModel, id):
            raise NotFoundError

        caixa = get_one(CaixaModel,id)
        delete_commit(caixa)
        



