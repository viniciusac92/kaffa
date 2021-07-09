from flask import Blueprint

bp = Blueprint('bp_testes', __name__)


@bp.get('/')
def api_form():
    ...


@bp.post('/register')
def create_user():
    ...
