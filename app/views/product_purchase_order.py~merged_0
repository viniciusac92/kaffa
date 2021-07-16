from ..services import ProductPurchaseOrderServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_product_purchase_order', __name__, url_prefix='/api')


@bp.route("/product_purchase_order", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(ProductPurchaseOrderServices.create_product_purchase_order(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/product_purchase_order", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(ProductPurchaseOrderServices.get_by_id(id))

        return jsonify(ProductPurchaseOrderServices.get_all_product_purchase_orders()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/product_purchase_order/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(ProductPurchaseOrderServices.update_product_purchase_order(data, id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/product_purchase_order/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        ProductPurchaseOrderServices.delete_product_purchase_order(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
