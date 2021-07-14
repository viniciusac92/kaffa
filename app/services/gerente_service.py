from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import GerenteModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class GerenteServices:

    required_fields = ["nome", "cpf", "id_usuario"]

    @staticmethod
    def create_gerente(data:dict):

        if verify_missing_key(data,GerenteServices.required_fields):
            raise MissingKeyError(data, GerenteServices.required_fields)

        if verify_recieved_keys(data, GerenteServices.required_fields):
            raise RequiredKeyError(data, GerenteServices.required_fields)

        gerente = GerenteModel(**data)

        add_commit(gerente)
        
        return get_one(GerenteModel, gerente.id)

    @staticmethod
    def get_all_gerentes():

        return get_all(GerenteModel)

    @staticmethod
    def get_by_id(id):

        return get_one(GerenteModel, id)

    @staticmethod
    def update_gerente(data: dict, id):

        if verify_recieved_keys(data, GerenteServices.required_fields):
            raise RequiredKeyError(data, GerenteServices.required_fields)
        
        if not get_one(GerenteModel, id):
            raise NotFoundError

        gerente = get_one(GerenteModel,id)
        update_model(gerente, data)

        return get_one(GerenteModel, id)

    @staticmethod
    def delete_gerente(id: int) -> None:

        if not get_one(GerenteModel, id):
            raise NotFoundError

        gerente = get_one(GerenteModel,id)
        delete_commit(gerente)



