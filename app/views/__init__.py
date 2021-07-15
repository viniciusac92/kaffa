from flask import Flask


def init_app(app: Flask) -> None:
    # import das bps e registro das blueprints abaixo
    from .caixa_view import bp as bp_caixa
    from .conta_produto_view import bp as bp_conta_produto
    from .conta_view import bp as bp_conta
    from .estoque_produto_view import bp as bp_estoque_produto
    from .forma_pagamento_view import bp as bp_forma_pgto
    from .fornecedor_produto_view import bp as bp_fornecedor_produto
    from .fornecedor_view import bp as bp_fornecedor
    from .garcom_view import bp as bp_garcon
    from .gerente_view import bp as bp_gerente
    from .login_view import bp as bp_login
    from .mesa_view import bp as bp_mesa
    from .operador_caixa_view import bp as bp_operador_caixa
    from .operador_view import bp as bp_operador
    from .ordem_compra_views import bp as bp_ordem_compra
    from .produto_ordem_compra import bp as bp_produto_ordem_compra
    from .produto_view import bp as bp_produto
    from .testes_view import bp as bp_testes
    from .user_view import bp as bp_user

    app.register_blueprint(bp_login)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_conta)
    app.register_blueprint(bp_garcon)
    app.register_blueprint(bp_forma_pgto)
    app.register_blueprint(bp_caixa)
    app.register_blueprint(bp_fornecedor)
    app.register_blueprint(bp_gerente)
    app.register_blueprint(bp_mesa)
    app.register_blueprint(bp_operador)
    app.register_blueprint(bp_produto)
    app.register_blueprint(bp_conta_produto)
    app.register_blueprint(bp_estoque_produto)
    app.register_blueprint(bp_fornecedor_produto)
    app.register_blueprint(bp_operador_caixa)
    app.register_blueprint(bp_ordem_compra)
    app.register_blueprint(bp_produto_ordem_compra)
    app.register_blueprint(bp_testes)
