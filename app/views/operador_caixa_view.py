from ..services import OperadorCaixaServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_operador_caixa', __name__, url_prefix='/api')


@bp.route("/operador_caixa", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    data = request.get_json()

    try:
        return jsonify(OperadorCaixaServices.create_operador_caixa(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/operador_caixa", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    id = request.args.get("id")
    try:
        if id:
            return jsonify(OperadorCaixaServices.get_by_id(id))

        return jsonify(OperadorCaixaServices.get_all_operador_caixas()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message


@bp.route("/operador_caixa/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    data = request.get_json()

    try:
        return jsonify(OperadorCaixaServices.update_operador_caixa(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/operador_caixa/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        

    try:
        OperadorCaixaServices.delete_operador_caixa(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
    