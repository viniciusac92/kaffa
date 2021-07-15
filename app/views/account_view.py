from ..services import AccountServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_account', __name__, url_prefix='/api')


@bp.route("/account", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(AccountServices.create_account(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/account", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(AccountServices.get_by_id(id))

        return jsonify(AccountServices.get_all_accounts()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/account/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(AccountServices.update_account(data, id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/account/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        AccountServices.delete_account(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
