from ..services import GerenteServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_gerente', __name__, url_prefix='/api')


@bp.route("/gerente", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(GerenteServices.create_gerente(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/gerente", methods=["GET"])
@jwt_required()
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(GerenteServices.get_by_id(id))

        return jsonify(GerenteServices.get_all_gerentes()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message



@bp.route("/gerente/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    data = request.get_json()

    try:
        return jsonify(GerenteServices.update_gerente(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/gerente/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):

    try:
        GerenteServices.delete_gerente(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT

