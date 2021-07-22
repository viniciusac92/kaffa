from ..services import ProviderServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError, UniqueKeyError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_provider', __name__, url_prefix='/api')


@bp.route("/provider", methods=["POST"])
@jwt_required()
def create():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(ProviderServices.create_provider(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

    except UniqueKeyError as e:
        return e.message

@bp.route("/provider", methods=["GET"])
@jwt_required()
def get():
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    id = request.args.get("id")
    try:
        if id:
            return jsonify(ProviderServices.get_by_id(id))

        return jsonify(ProviderServices.get_all_providers()), HTTPStatus.OK

    except NotFoundError as e:
        return e.message


@bp.route("/provider/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    data = request.get_json()

    try:
        return jsonify(ProviderServices.update_provider(data, id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/provider/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if get_jwt_identity()["type"] != 1:
        return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED

    try:
        ProviderServices.delete_provider(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT
