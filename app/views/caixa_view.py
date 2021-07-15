from app.models.caixa_model import CaixaModel
from ..services import CaixaServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_caixa', __name__, url_prefix='/api')


@bp.route("/caixa", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    data = request.get_json()

    try:
        return jsonify(CaixaServices.create_caixa(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/caixa", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    id = request.args.get("id")
    try:
        if id:
            return jsonify(CaixaServices.get_by_id(id))

        return jsonify(CaixaServices.get_all_caixas()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message



@bp.route("/caixa/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
        
    data = request.get_json()

    try:
        return jsonify(CaixaServices.update_caixa(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/caixa/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        

    try:
        CaixaServices.delete_caixa(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT

