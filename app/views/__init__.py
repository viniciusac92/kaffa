from flask import Flask


def init_app(app: Flask):
    from .testes_view import bp as bp_testes

    app.register_blueprint(bp_testes)
