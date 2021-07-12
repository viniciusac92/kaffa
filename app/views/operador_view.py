from ..services import OperadorServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_operador', __name__, url_prefix='/api')


@bp.route("/operador", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(OperadorServices.create_operador(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/operador", methods=["GET"])
@jwt_required()
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(OperadorServices.get_by_id(id))

        return jsonify(OperadorServices.get_all_operadores()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message



@bp.route("/operador/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    data = request.get_json()

    try:
        return jsonify(OperadorServices.update_operador(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/operador/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):

    try:
        OperadorServices.delete_operador(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT

