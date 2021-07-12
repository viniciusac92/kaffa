from ..services import ProdutoServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_produto', __name__, url_prefix='/api')


@bp.route("/produto", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(ProdutoServices.create_produto(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/produto", methods=["GET"])
@jwt_required()
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(ProdutoServices.get_by_id(id))

        return jsonify(ProdutoServices.get_all_produtos()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message



@bp.route("/produto/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    data = request.get_json()

    try:
        return jsonify(ProdutoServices.update_produto(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/produto/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):

    try:
        ProdutoServices.delete_produto(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT

