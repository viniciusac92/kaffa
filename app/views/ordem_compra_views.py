from ..services import OrdemCompraServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_ordem_compra', __name__, url_prefix='/api')


@bp.route("/ordem_compra", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(OrdemCompraServices.create_ordem_compra(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/ordem_compra", methods=["GET"])
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(OrdemCompraServices.get_by_id(id))

        return jsonify(OrdemCompraServices.get_all_ordem_compras()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message


@bp.route("/ordem_compra/<int:id>", methods=["PUT", "PATCH"])
def update(id):
    data = request.get_json()

    try:
        return jsonify(OrdemCompraServices.update_ordem_compra(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/ordem_compra/<int:id>", methods=["DELETE"])
def delete(id):

    try:
        OrdemCompraServices.delete_ordem_compra(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
    