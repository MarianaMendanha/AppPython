# Importação do módulo Blueprint da biblioteca Flask
from flask import Blueprint, jsonify

# Criação de um Blueprint chamado "event_route" para as rotas relacionadas a eventos
event_route_bp = Blueprint("event_route", __name__)

# Definição da rota para lidar com requisições POST na raiz ("/events") do Blueprint "event_route"


@event_route_bp.route("/events", methods=["POST"])
def create_event():
    return jsonify({"ola": "mundo"}), 200
