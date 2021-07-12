from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import GarcomModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)
from ipdb import set_trace

class GarcomServices:

    required_fields = ["nome", "cpf"]

    @staticmethod
    def create_garcom(data:dict):

        if verify_missing_key(data,GarcomServices.required_fields):
            raise MissingKeyError(data, GarcomServices.required_fields)

        if verify_recieved_keys(data, GarcomServices.required_fields):
            raise RequiredKeyError(data, GarcomServices.required_fields)

        garcom = GarcomModel(**data)

        add_commit(garcom)
        
        return get_one(GarcomModel, garcom.id)

    @staticmethod
    def get_all_garcons():

        return get_all(GarcomModel)

    @staticmethod
    def get_by_id(id):

        return get_one(GarcomModel, id)

    @staticmethod
    def update_garcon(data: dict, id):

        if verify_recieved_keys(data, GarcomServices.required_fields):
            raise RequiredKeyError(data, GarcomServices.required_fields)
        
        if not get_one(GarcomModel, id):
            raise NotFoundError

        garcom = get_one(GarcomModel,id)
        update_model(garcom, data)

        return get_one(GarcomModel, id)

    @staticmethod
    def delete_garcom(id: int) -> None:

        if not get_one(GarcomModel, id):
            raise NotFoundError

        garcom = get_one(GarcomModel,id)
        delete_commit(garcom)



