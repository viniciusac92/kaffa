from flask import Flask


def init_app(app: Flask) -> None:
    # import das bps e registro das blueprints abaixo
    from .login_view import bp as bp_login
    from .user_view import bp as bp_user
    from .conta_view import bp as bp_conta
    from .garcom_view import bp as bp_garcon
    from .forma_pagamento_view import bp as bp_forma_pgto
    from .caixa_view import bp as bp_caixa
    from .fornecedor_view import bp as bp_fornecedor
    from .gerente_view import bp as bp_gerente
    from .mesa_view import bp as bp_mesa
    from .operador_view import bp as bp_operador
    from .produto_view import bp as bp_produto
    from .conta_produto_view import bp as bp_conta_produto
    from .estoque_produto_view import bp as bp_estoque_produto
    from .fornecedor_produto_view import bp as bp_fornecedor_produto
    from .operador_caixa_view import bp as bp_operador_caixa
    from .ordem_compra_views import bp as bp_ordem_compra
    from .produto_ordem_compra import bp as bp_produto_ordem_compra

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
    