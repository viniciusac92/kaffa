from os import access
from app.models.user_model import UserModel
from ..services import UserServices
from ..custom_errors import MissingKeyError, RequiredKeyError, NotFoundError

from flask import Blueprint, request, redirect, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from http import HTTPStatus

bp = Blueprint('bp_login', __name__, url_prefix='/api')


@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user: UserModel = UserServices.found_user(username)

    if not user:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND

    if user.verify_password(password):
        access_token = create_access_token(identity=user)
        return {"token": access_token}, HTTPStatus.OK

    return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
