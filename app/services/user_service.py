from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import UserModel
from . import (add_commit, get_all, get_one, verify_recieved_keys, 
update_model, delete_commit, verify_missing_key)
from app.services.garcom_service import GarcomServices
from app.services.gerente_service import GerenteServices
from app.services.operador_service import OperadorServices
from ipdb import set_trace

class UserServices:

    required_fields = ["username", "tipo", "password", "nome", "cpf"]

    @staticmethod
    def create_user(data:dict): 

        if verify_missing_key(data,UserServices.required_fields):
            raise MissingKeyError(data, UserServices.required_fields)

        if verify_recieved_keys(data, UserServices.required_fields):
            raise RequiredKeyError(data, UserServices.required_fields)

        nome = data.pop('nome')
        cpf = data.pop('cpf')
        password_to_hash = data.pop('password')
        usuario = UserModel(**data)
        usuario.password = password_to_hash

        add_commit(usuario)

        user = get_one(UserModel, usuario.id)

        if data["tipo"] == 1:
            info_user = GerenteServices.create_gerente({"nome": nome, "cpf": cpf, "id_usuario": user.id})

        if data["tipo"] == 2:
            info_user = GarcomServices.create_garcom({"nome": nome, "cpf": cpf, "id_usuario": user.id})

        if data["tipo"] == 3:
            info_user = OperadorServices.create_operador({"nome": nome, "cpf": cpf, "id_usuario": user.id})

        if user.tipo == 1:
            tipo = "Gerente"
        elif user.tipo == 2:
            tipo = "Garçon"
        else:
            tipo = "Operador(a) de caixa"

        return {
            "nome": info_user.nome,
            "tipo": tipo,
            "username": user.username,
            "cpf": info_user.cpf,
            "password": user.password_hash
        }

    @staticmethod
    def get_all_users():

        return get_all(UserModel)

    @staticmethod
    def update_user(data: dict, id):

        if verify_recieved_keys(data, UserServices.required_fields):
            raise RequiredKeyError(data, UserServices.required_fields)
        
        if not get_one(UserModel, id):
            raise NotFoundError

        usuario = get_one(UserModel,id)
        update_model(usuario, data)

        return get_one(UserModel, id)

    @staticmethod
    def delete_user(id: int) -> None:

        if not get_one(UserModel, id):
            raise NotFoundError

        usuario = get_one(UserModel,id)
        delete_commit(usuario)

    @staticmethod
    def found_user(username):
        return UserModel.query.filter_by(username=username).first()

    @staticmethod
    def get_by_id(id):
        user = get_one(UserModel, id)
        if not user:
            raise NotFoundError

        return user
