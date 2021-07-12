from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import FormaPagamentoModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class FormaPgtoServices:

    required_fields = ["nome", "descricao"]

    @staticmethod
    def create_forma_pgto(data:dict):

        if verify_missing_key(data,FormaPgtoServices.required_fields):
            raise MissingKeyError(data, FormaPgtoServices.required_fields)

        if verify_recieved_keys(data, FormaPgtoServices.required_fields):
            raise RequiredKeyError(data, FormaPgtoServices.required_fields)

        forma_pgto = FormaPagamentoModel(**data)

        add_commit(forma_pgto)
        
        return get_one(FormaPagamentoModel, forma_pgto.id)

    @staticmethod
    def get_all_forma_pgto():

        return get_all(FormaPagamentoModel)

    @staticmethod
    def get_by_id(id):

        return get_one(FormaPagamentoModel, id)

    @staticmethod
    def update_forma_pgto(data: dict, id):

        if verify_recieved_keys(data, FormaPgtoServices.required_fields):
            raise RequiredKeyError(data, FormaPgtoServices.required_fields)
        
        if not get_one(FormaPagamentoModel, id):
            raise NotFoundError

        forma_pgto = get_one(FormaPagamentoModel,id)
        update_model(forma_pgto, data)

        return get_one(FormaPagamentoModel, id)

    @staticmethod
    def delete_forma_pgto(id: int) -> None:

        if not get_one(FormaPagamentoModel, id):
            raise NotFoundError

        forma_pgto = get_one(FormaPagamentoModel,id)
        delete_commit(forma_pgto)




