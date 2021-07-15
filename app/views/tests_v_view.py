from http import HTTPStatus

from app.configs.database import db
from app.models import (
    AccountModel,
    AccountProductModel,
    ManagerModel,
    OperatorModel,
    ProductModel,
    UserModel,
    WaiterModel,
)
from flask import Blueprint

bp = Blueprint('bp_tests_v', __name__, url_prefix='/api')


@bp.route("/", methods=["GET"])
def get():
    session = db.session
    gerentes_list = (
        session.query(ManagerModel)
        .join(UserModel, UserModel.id == ManagerModel.id_user)
        .all()
    )
    # garcons_list = session.query(WaiterModel).join(UserModel).all()
    # operadores_list = session.query(OperatorModel).join(UserModel).all()
    # conta_list = (
    #     session.query(ProductModel).join(AccountProductModel).join(AccountModel).all()
    # )

    # ROTA DE VENDAS

    data1 = [info.usuario.username for info in gerentes_list]

    # data2 = [info.usuario.username for info in garcons_list]

    # data3 = [info.usuario.username for info in operadores_list]

    # data4 = [c.garcom_da_conta_model for info in conta_list for c in info.contas_list]

    import ipdb

    ipdb.set_trace()

    return {"msg": "teste retornou"}, HTTPStatus.OK
