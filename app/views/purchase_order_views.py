from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..custom_errors import MissingKeyError, NotFoundError, RequiredKeyError, PurchaseClosedError, FkNotFoundError
from ..services import PurchaseOrderServices

bp = Blueprint('bp_purchase_order', __name__, url_prefix='/api')


@bp.route("/purchase_order", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return (
            jsonify(PurchaseOrderServices.create_purchase_order(data)),
            HTTPStatus.CREATED,
        )

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

    except FkNotFoundError as e:
        return e.message

@bp.route("/purchase_order", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(PurchaseOrderServices.get_by_id(id))

        return jsonify(PurchaseOrderServices.get_all_purchase_orders()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/purchase_order/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return (
            jsonify(PurchaseOrderServices.update_purchase_order(data, id)),
            HTTPStatus.OK,
        )

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

    except PurchaseClosedError as e:
        return e.message


@bp.route("/purchase_order/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        PurchaseOrderServices.delete_purchase_order(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT

@bp.route("/purchase_order/<int:id>/close_order", methods=["GET"])
@jwt_required()
def close_purchase_order(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    # data = request.get_json()

    try:
        return (
            jsonify(PurchaseOrderServices.close_purchase_order(id)),
            HTTPStatus.OK,
        )

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message