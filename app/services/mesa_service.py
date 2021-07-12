from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import MesaModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class MesaServices:

    required_fields = ["numero"]

    @staticmethod
    def create_mesa(data:dict):

        if verify_missing_key(data,MesaServices.required_fields):
            raise MissingKeyError(data, MesaServices.required_fields)

        if verify_recieved_keys(data, MesaServices.required_fields):
            raise RequiredKeyError(data, MesaServices.required_fields)

        mesa = MesaModel(**data)

        add_commit(mesa)
        
        return get_one(MesaModel, mesa.id)

    @staticmethod
    def get_all_mesas():

        return get_all(MesaModel)

    @staticmethod
    def get_by_id(id):

        return get_one(MesaModel, id)

    @staticmethod
    def update_mesa(data: dict, id):

        if verify_recieved_keys(data, MesaServices.required_fields):
            raise RequiredKeyError(data, MesaServices.required_fields)
        
        if not get_one(MesaModel, id):
            raise NotFoundError

        mesa = get_one(MesaModel,id)
        update_model(mesa, data)

        return get_one(MesaModel, id)

    @staticmethod
    def delete_mesa(id: int) -> None:

        if not get_one(MesaModel, id):
            raise NotFoundError

        mesa = get_one(MesaModel,id)
        delete_commit(mesa)



