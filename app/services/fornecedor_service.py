from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import FornecedorModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)

class FornecedorServices:

    required_fields = ["nome_fantasia", "cnpj", "telefone"]

    @staticmethod
    def create_fornecedor(data:dict):

        if verify_missing_key(data,FornecedorServices.required_fields):
            raise MissingKeyError(data, FornecedorServices.required_fields)

        if verify_recieved_keys(data, FornecedorServices.required_fields):
            raise RequiredKeyError(data, FornecedorServices.required_fields)

        fornecedor = FornecedorModel(**data)

        add_commit(fornecedor)
        
        return get_one(FornecedorModel, fornecedor.id)

    @staticmethod
    def get_all_fornecedores():

        return get_all(FornecedorModel)

    @staticmethod
    def get_by_id(id):

        return get_one(FornecedorModel, id)

    @staticmethod
    def update_fornecedor(data: dict, id):

        if verify_recieved_keys(data, FornecedorServices.required_fields):
            raise RequiredKeyError(data, FornecedorServices.required_fields)
        
        if not get_one(FornecedorModel, id):
            raise NotFoundError

        fornecedor = get_one(FornecedorModel,id)
        update_model(fornecedor, data)

        return get_one(FornecedorModel, id)

    @staticmethod
    def delete_fornecedor(id: int) -> None:

        if not get_one(FornecedorModel, id):
            raise NotFoundError

        fornecedor = get_one(FornecedorModel,id)
        delete_commit(fornecedor)



