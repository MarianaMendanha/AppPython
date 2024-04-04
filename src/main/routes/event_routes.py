# Importação do módulo Blueprint da biblioteca Flask
from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler
from src.errors.error_handler import handle_error

# Criação de um Blueprint chamado "event_route" para as rotas relacionadas a eventos
event_route_bp = Blueprint("event_route", __name__)

# Definição da rota para lidar com requisições POST na raiz ("/events") do Blueprint "event_route"


@event_route_bp.route("/events", methods=["POST"])
def create_event():
    try:
        http_request = HttpRequest(body=request.json)
        event_handler = EventHandler()
        http_response = event_handler.register(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        event_handler = EventHandler()
        http_request = HttpRequest(param={"event_id": event_id})

        http_response = event_handler.find_by_id(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
