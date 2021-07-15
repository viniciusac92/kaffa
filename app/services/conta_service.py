from sqlalchemy import and_

from app.custom_errors.not_found import NotFoundError
from app.custom_errors import required_key
from ..custom_errors import MissingKeyError, RequiredKeyError
from ..models import ContaModel, ContaProdutoModel, GarcomModel, FormaPagamentoModel
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
        
        # return get_one(ContaModel, conta.id)

        bill = get_one(ContaModel, conta.id)

        return {
            "id": bill.id,
            "data": bill.data,
            "id_caixa": bill.id_caixa,
            "garcom": GarcomModel.query.get(bill.id_garcom).nome,
            "id_mesa": bill.id_mesa,
            "forma_pagamento": FormaPagamentoModel.query.get(bill.id_forma_pagamento).nome,
            "lista_produtos": [
                {
                    "id": produto.id,
                    "nome": produto.nome,
                    "descricao": produto.descricao,
                    "preco": produto.preco,
                    "quantidade": ContaProdutoModel.query.filter(and_(ContaProdutoModel.id_produto == produto.id, ContaProdutoModel.id_conta == bill.id)).first().quantity
                }
                for produto in bill.lista_produtos
            ]
        }

    @staticmethod
    def get_all_contas():

        bill_list = get_all(ContaModel)

        return [
            {
                "id": bill.id,
                "data": bill.data,
                "id_caixa": bill.id_caixa,
                "garcom": GarcomModel.query.get(bill.id_garcom).nome,
                "id_mesa": bill.id_mesa,
                "forma_pagamento": FormaPagamentoModel.query.get(bill.id_forma_pagamento).nome,
                "lista_produtos": [
                    {
                        "id": produto.id,
                        "nome": produto.nome,
                        "descricao": produto.descricao,
                        "preco": produto.preco,
                        "quantidade": ContaProdutoModel.query.filter(and_(ContaProdutoModel.id_produto == produto.id, ContaProdutoModel.id_conta == bill.id)).first().quantity
                    }
                    for produto in bill.lista_produtos
                ]
            }
            for bill in bill_list
        ]

    
    @staticmethod
    def get_by_id(id):

        bill = get_one(ContaModel, id)

        return {
            "id": bill.id,
            "data": bill.data,
            "id_caixa": bill.id_caixa,
            "garcom": GarcomModel.query.get(bill.id_garcom).nome,
            "id_mesa": bill.id_mesa,
            "forma_pagamento": FormaPagamentoModel.query.get(bill.id_forma_pagamento).nome,
            "lista_produtos": [
                {
                    "id": produto.id,
                    "nome": produto.nome,
                    "descricao": produto.descricao,
                    "preco": produto.preco,
                    "quantidade": ContaProdutoModel.query.filter(and_(ContaProdutoModel.id_produto == produto.id, ContaProdutoModel.id_conta == bill.id)).first().quantity
                }
                for produto in bill.lista_produtos
            ]
        }


    @staticmethod
    def update_conta(data: dict, id):

        if verify_recieved_keys(data, ContaServices.required_fields):
            raise RequiredKeyError(data, ContaServices.required_fields)
        
        if not get_one(ContaModel, id):
            raise NotFoundError

        usuario = get_one(ContaModel,id)
        update_model(usuario, data)

        # return get_one(ContaModel, id)
        bill = get_one(ContaModel, id)

        return {
            "id": bill.id,
            "data": bill.data,
            "id_caixa": bill.id_caixa,
            "garcom": GarcomModel.query.get(bill.id_garcom).nome,
            "id_mesa": bill.id_mesa,
            "forma_pagamento": FormaPagamentoModel.query.get(bill.id_forma_pagamento).nome,
            "lista_produtos": [
                {
                    "id": produto.id,
                    "nome": produto.nome,
                    "descricao": produto.descricao,
                    "preco": produto.preco,
                    "quantidade": ContaProdutoModel.query.filter(and_(ContaProdutoModel.id_produto == produto.id, ContaProdutoModel.id_conta == bill.id)).first().quantity
                }
                for produto in bill.lista_produtos
            ]
        }

    @staticmethod
    def delete_conta(id: int) -> None:

        if not get_one(ContaModel, id):
            raise NotFoundError

        usuario = get_one(ContaModel,id)
        delete_commit(usuario)

    @staticmethod
    def found_conta(username):
        return ContaModel.query.filter_by(username=username).first()
