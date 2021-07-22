from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..custom_errors import (
    AccountClosedError,
    MissingKeyError,
    NotFoundError,
    OutOfStockError,
    RequiredKeyError,
    FkNotFoundError
)
from ..services import AccountProductServices

bp = Blueprint('bp_account_product', __name__, url_prefix='/api')


@bp.route("/account_product", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 2:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return (
            jsonify(AccountProductServices.create_account_product(data)),
            HTTPStatus.CREATED,
        )

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

    except OutOfStockError as e:
        return e.message

    except AccountClosedError as e:
        return e.message

    except FkNotFoundError as e:
        return e.message


@bp.route("/account_product", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(AccountProductServices.get_by_id(id))

        return jsonify(AccountProductServices.get_all_account_products()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/account_product/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return (
            jsonify(AccountProductServices.update_account_product(data, id)),
            HTTPStatus.OK,
        )

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

    except FkNotFoundError as e:
        return e.message

@bp.route("/account_product/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        AccountProductServices.delete_account_product(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
