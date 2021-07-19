from app.models.cashier_model import CashierModel
from ..services import CashierServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_cashier', __name__, url_prefix='/api')


@bp.route("/cashier", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(CashierServices.create_cashier(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/cashier", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(CashierServices.get_by_id(id))

        return jsonify(CashierServices.get_all_cashiers()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/cashier/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):

    data = request.get_json()

    try:
        return jsonify(CashierServices.update_cashier(data, id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/cashier/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        CashierServices.delete_cashier(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT



@bp.route("/cashier/<int:id>/cash_balance", methods=["GET"])
@jwt_required()
def cash_balance(id):

    try:
        return jsonify(CashierServices.cash_balance(id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

@bp.route("/cashier/<int:id>/cash_withdrawal", methods=["GET"])
@jwt_required()
def cash_withdrawal(id):

    data = request.get_json()

    try:
        return jsonify(CashierServices.cash_withdrawal(data, id)), HTTPStatus.OK

    # except NotFoundError as e:
    #     return e.message

    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
