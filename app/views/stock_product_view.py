from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..custom_errors import MissingKeyError, NotFoundError, RequiredKeyError
from ..services import StockProductServices

bp = Blueprint('bp_stock_product', __name__, url_prefix='/api')


@bp.route("/stock_product", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return (
            jsonify(StockProductServices.create_stock_product(data)),
            HTTPStatus.CREATED,
        )

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/stock_product", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(StockProductServices.get_by_id(id))

        return jsonify(StockProductServices.get_all_stock_products()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/stock_product/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return (
            jsonify(StockProductServices.update_stock_product(data, id)),
            HTTPStatus.OK,
        )

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/stock_product/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["tipo"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        StockProductServices.delete_stock_product(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
