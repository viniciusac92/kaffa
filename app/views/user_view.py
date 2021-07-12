from ..services import UserServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus

bp = Blueprint('bp_user', __name__, url_prefix='/api')


@bp.route("/user", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(UserServices.create_user(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/user", methods=["GET"])
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(UserServices.get_by_id(id)), HTTPStatus.OK
        return jsonify(UserServices.get_all_users()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/user/<int:id>", methods=["PUT", "PATCH"])
def update(id):
    data = request.get_json()

    try:
        return jsonify(UserServices.update_user(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/user/<int:id>", methods=["DELETE"])
def delete(id):

    try:
        UserServices.delete_user(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT