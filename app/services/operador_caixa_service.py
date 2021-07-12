from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import OperadorCaixaModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class OperadorCaixaServices:

    required_fields = ["id_operador", "id_caixa"]

    @staticmethod
    def create_operador_caixa(data:dict):

        if verify_missing_key(data,OperadorCaixaServices.required_fields):
            raise MissingKeyError(data, OperadorCaixaServices.required_fields)

        if verify_recieved_keys(data, OperadorCaixaServices.required_fields):
            raise RequiredKeyError(data, OperadorCaixaServices.required_fields)

        operador_caixa = OperadorCaixaModel(**data)

        add_commit(operador_caixa)
        
        return get_one(OperadorCaixaModel, operador_caixa.id)

    @staticmethod
    def get_all_operador_caixas():

        return get_all(OperadorCaixaModel)

    @staticmethod
    def get_by_id(id):

        return get_one(OperadorCaixaModel, id)

    @staticmethod
    def update_operador_caixa(data: dict, id):

        if verify_recieved_keys(data, OperadorCaixaServices.required_fields):
            raise RequiredKeyError(data, OperadorCaixaServices.required_fields)
        
        if not get_one(OperadorCaixaModel, id):
            raise NotFoundError

        operador_caixa = get_one(OperadorCaixaModel,id)
        update_model(operador_caixa, data)

        return get_one(OperadorCaixaModel, id)

    @staticmethod
    def delete_operador_caixa(id: int) -> None:

        if not get_one(OperadorCaixaModel, id):
            raise NotFoundError

        operador_caixa = get_one(OperadorCaixaModel,id)
        delete_commit(operador_caixa)



