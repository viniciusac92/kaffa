from http import HTTPStatus

from app.configs.database import db
from app.models import GarcomModel, GerenteModel, OperadorModel, UserModel
from flask import Blueprint, jsonify, request

from ..custom_errors import MissingKeyError, NotFoundError, RequiredKeyError
from ..services import UserServices

bp = Blueprint('bp_testes', __name__, url_prefix='/api')


@bp.route("/", methods=["GET"])
def get():
    session = db.session
    gerentes_list = session.query(GerenteModel).join(UserModel).all()
    garcons_list = session.query(GarcomModel).join(UserModel).all()
    operadores_list = session.query(OperadorModel).join(UserModel).all()

    data1 = [info.usuario.username for info in gerentes_list]

    data2 = [info.usuario.username for info in garcons_list]

    data3 = [info.usuario.username for info in operadores_list]

    import ipdb

    ipdb.set_trace()

    return {"msg": "teste retornou"}, HTTPStatus.OK
