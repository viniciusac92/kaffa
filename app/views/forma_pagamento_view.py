from ..services import FormaPgtoServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from http import HTTPStatus


bp = Blueprint('bp_forma_pagamento', __name__, url_prefix='/api')


@bp.route("/forma_pgto", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    try:
        return jsonify(FormaPgtoServices.create_forma_pgto(data)), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/forma_pgto", methods=["GET"])
@jwt_required()
def get():
    id = request.args.get("id")
    try:
        if id:
            return jsonify(FormaPgtoServices.get_by_id(id))

        return jsonify(FormaPgtoServices.get_all_forma_pgto()), HTTPStatus.OK
    
    except NotFoundError as e:
        return e.message



@bp.route("/forma_pgto/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    data = request.get_json()

    try:
        return jsonify(FormaPgtoServices.update_forma_pgto(data,id)), HTTPStatus.OK

    except NotFoundError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message


@bp.route("/forma_pgto/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):

    try:
        FormaPgtoServices.delete_forma_pgto(id)

    except NotFoundError as e:
        return e.message

    return "", HTTPStatus.NO_CONTENT

