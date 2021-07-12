from ..services import MesaServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_mesa', __name__, url_prefix='/api')


@bp.route("/mesa", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(MesaServices.create_mesa(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/mesa", methods=["GET"])
@jwt_required()
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(MesaServices.get_by_id(id))

        return jsonify(MesaServices.get_all_mesas()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message



@bp.route("/mesa/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    data = request.get_json()

    try:
        return jsonify(MesaServices.update_mesa(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/mesa/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):

    try:
        MesaServices.delete_mesa(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT

