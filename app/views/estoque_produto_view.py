from ..services import EstoqueProdutoServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_estoque_produto', __name__, url_prefix='/api')


@bp.route("/estoque_produto", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(EstoqueProdutoServices.create_estoque_produto(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/estoque_produto", methods=["GET"])
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(EstoqueProdutoServices.get_by_id(id))

        return jsonify(EstoqueProdutoServices.get_all_estoque_produtos()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message


@bp.route("/estoque_produto/<int:id>", methods=["PUT", "PATCH"])
def update(id):
    data = request.get_json()

    try:
        return jsonify(EstoqueProdutoServices.update_estoque_produto(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/estoque_produto/<int:id>", methods=["DELETE"])
def delete(id):

    try:
        EstoqueProdutoServices.delete_estoque_produto(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
    