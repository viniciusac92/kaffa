from ..services import ProdutoOrdemCompraServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_produto_ordem_compra', __name__, url_prefix='/api')


@bp.route("/produto_ordem_compra", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(ProdutoOrdemCompraServices.create_produto_ordem_compra(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/produto_ordem_compra", methods=["GET"])
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(ProdutoOrdemCompraServices.get_by_id(id))

        return jsonify(ProdutoOrdemCompraServices.get_all_produto_ordem_compras()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message


@bp.route("/produto_ordem_compra/<int:id>", methods=["PUT", "PATCH"])
def update(id):
    data = request.get_json()

    try:
        return jsonify(ProdutoOrdemCompraServices.update_produto_ordem_compra(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/produto_ordem_compra/<int:id>", methods=["DELETE"])
def delete(id):

    try:
        ProdutoOrdemCompraServices.delete_produto_ordem_compra(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
    