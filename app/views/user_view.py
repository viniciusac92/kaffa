from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError

from ..custom_errors import (
    MissingKeyError,
    NotFoundError,
    RequiredKeyError,
    UniqueKeyError,
)
from ..services import UserServices

bp = Blueprint('bp_user', __name__, url_prefix='/api')


@bp.route("/user", methods=["POST"])
def create():

    data = request.get_json()

    try:
        return jsonify(UserServices.create_user(data)), HTTPStatus.CREATED

    except UniqueKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/user", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(UserServices.get_by_id(id)), HTTPStatus.OK
        return jsonify(UserServices.get_all_users()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/user/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(UserServices.update_user(data, id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/user/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        UserServices.delete_user(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
