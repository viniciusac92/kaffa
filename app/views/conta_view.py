from ..services import ContaServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_conta', __name__, url_prefix='/api')


@bp.route("/conta", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    data = request.get_json()

    try:
        return jsonify(ContaServices.create_conta(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/conta", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    id = request.args.get("id")
    try:
        if id:
            return jsonify(ContaServices.get_by_id(id))

        return jsonify(ContaServices.get_all_contas()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message


@bp.route("/conta/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        
    data = request.get_json()

    try:
        return jsonify(ContaServices.update_conta(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/conta/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED
        

    try:
        ContaServices.delete_conta(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
    