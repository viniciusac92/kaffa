# from app.models.bacias_estados_model import BaciasEstadosModel
# from app.models.estados_model import EstadosModel
# from app.models.bacias_hidrograficas_model import BaciashidrograficasModel
# from flask import Blueprint, request
# from http import HTTPStatus
# from app import db

# bp_create_bacia_estado = Blueprint("bp_create_bacia_estado", __name__)


# @bp_create_bacia_estado.route("/bacia_estado", methods=["POST"])
# def create_bacia_estado():    

#     data = request.get_json()
#     bacia = BaciashidrograficasModel.query.filter_by(nome=data['bacia_nome']).first()
#     estado = EstadosModel.query.filter_by(nome=data['estado_nome']).first()

#     bacia_estado = BaciasEstadosModel(estado_id=estado.id, bacia_id=bacia.id)
    
#     try:
#         db.session.add(bacia_estado)
#         db.session.commit() 
#     except:
#         return '', 422

#     return {
#         "id": bacia_estado.id,
#         "estado_nome": estado.nome,
#         "bacia_nome": bacia.area,
#     }, HTTPStatus.CREATED
