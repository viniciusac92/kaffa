from ..services import WaiterServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError, ImmutableAttrError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_waiter', __name__, url_prefix='/api')


@bp.route("/waiter", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(WaiterServices.create_waiter(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/waiters", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(WaiterServices.get_by_id(id))

        return jsonify(WaiterServices.get_all_waiters()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/waiter/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(WaiterServices.update_waiter(data, id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

    except ImmutableAttrError as e:
        return e.message


@bp.route("/waiters/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        WaiterServices.delete_waiter(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
