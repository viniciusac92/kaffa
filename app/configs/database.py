from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    #importar as models aqui embaixo
    from app.models.caixa_model import CaixaModel
    from app.models.operador_model import OperadorModel
    from app.models.operador_caixa_model import OperadorCaixaModel
    from app.models.garcom_model import GarcomModel
    from app.models.mesa_model import MesaModel
    from app.models.forma_pagamento_model import FormaPagamentoModel
    from app.models.conta_model import ContaModel
    from app.models.gerente_model import GerenteModel
    from app.models.conta_produto import ContaProdutoModel
    from app.models.estoque_produto import EstoqueProdutoModel
    from app.models.fornecedor_model import FornecedorModel
    from app.models.fornecedor_produto_model import FornecedorProdutoModel
    from app.models.ordem_de_compra_model import OrdemDeCompraModel
    from app.models.produto_ordem_de_compra_model import ProdutoOrdemDeCompraModel
    from app.models.produto_model import ProdutoModel
    from app.models.user_model import UserModel
    