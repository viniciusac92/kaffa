from ..services import PaymentMethodServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_payment_method', __name__, url_prefix='/api')


@bp.route("/payment_method", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(PaymentMethodServices.create_payment_method(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/payment_method", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(PaymentMethodServices.get_by_id(id))

        return jsonify(PaymentMethodServices.get_all_payment_method()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/payment_method/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(PaymentMethodServices.update_payment_method(data, id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/payment_method/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        PaymentMethodServices.delete_payment_method(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
