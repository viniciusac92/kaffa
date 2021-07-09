from http import HTTPStatus

from app import db
from flask import Blueprint, request

bp = Blueprint('bp_testes', __name__)


@bp.get('/')
def api_form():
    ...


@bp.post('/register')
def create_user():
    ...
