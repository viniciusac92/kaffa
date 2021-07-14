from ..services import FornecedorServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_fornecedor', __name__, url_prefix='/api')


@bp.route("/fornecedor", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    data = request.get_json()

    try:
        return jsonify(FornecedorServices.create_fornecedor(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/fornecedor", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    id = request.args.get("id")
    try:
        if id:
            return jsonify(FornecedorServices.get_by_id(id))

        return jsonify(FornecedorServices.get_all_fornecedores()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message



@bp.route("/fornecedor/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    data = request.get_json()

    try:
        return jsonify(FornecedorServices.update_fornecedor(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/fornecedor/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        

    try:
        FornecedorServices.delete_fornecedor(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT

