from ..services import FornecedorProdutoServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_fornecedor_produto', __name__, url_prefix='/api')


@bp.route("/fornecedor_produto", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(FornecedorProdutoServices.create_fornecedor_produto(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/fornecedor_produto", methods=["GET"])
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(FornecedorProdutoServices.get_by_id(id))

        return jsonify(FornecedorProdutoServices.get_all_fornecedor_produtos()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message


@bp.route("/fornecedor_produto/<int:id>", methods=["PUT", "PATCH"])
def update(id):
    data = request.get_json()

    try:
        return jsonify(FornecedorProdutoServices.update_fornecedor_produto(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/fornecedor_produto/<int:id>", methods=["DELETE"])
def delete(id):

    try:
        FornecedorProdutoServices.delete_fornecedor_produto(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
    