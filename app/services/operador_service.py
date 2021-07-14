from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import OperadorModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class OperadorServices:

    required_fields = ["nome", "cpf", "id_usuario"]

    @staticmethod
    def create_operador(data:dict):

        if verify_missing_key(data,OperadorServices.required_fields):
            raise MissingKeyError(data, OperadorServices.required_fields)

        if verify_recieved_keys(data, OperadorServices.required_fields):
            raise RequiredKeyError(data, OperadorServices.required_fields)

        operador = OperadorModel(**data)

        add_commit(operador)
        
        return get_one(OperadorModel, operador.id)

    @staticmethod
    def get_all_operadores():

        return get_all(OperadorModel)

    @staticmethod
    def get_by_id(id):

        return get_one(OperadorModel, id)

    @staticmethod
    def update_operador(data: dict, id):

        if verify_recieved_keys(data, OperadorServices.required_fields):
            raise RequiredKeyError(data, OperadorServices.required_fields)
        
        if not get_one(OperadorModel, id):
            raise NotFoundError

        operador = get_one(OperadorModel,id)
        update_model(operador, data)

        return get_one(OperadorModel, id)

    @staticmethod
    def delete_operador(id: int) -> None:

        if not get_one(OperadorModel, id):
            raise NotFoundError

        operador = get_one(OperadorModel,id)
        delete_commit(operador)



