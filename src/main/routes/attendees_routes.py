# Importação do módulo Blueprint da biblioteca Flask
from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendee_handler import AttendeeHandler
from src.errors.error_handler import handle_error

# Criação de um Blueprint chamado "attendee_route" para as rotas relacionadas a participantes
attendee_route_bp = Blueprint("attendee_route", __name__)

# Definição da rota para lidar com requisições POST na raiz ("/attendees") do Blueprint "attendee_route"
# Definição da rota para lidar com requisições POST -> registrar participante em evento


@attendee_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendee(event_id):
    try:
        http_request = HttpRequest(
            param={"event_id": event_id}, body=request.json)

        attendee_handler = AttendeeHandler()
        http_response = attendee_handler.registry(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

#  Definição da rota para lidar com requisições GET -> buscar badge de participante


@attendee_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendee_badge(attendee_id):
    try:
        attendee_handler = AttendeeHandler()
        http_request = HttpRequest(param={"attendee_id": attendee_id})

        http_response = attendee_handler.find_attendee_badge(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

#  Definição da rota para lidar com requisições GET -> buscar participantes por evento


@attendee_route_bp.route("/event/<event_id>/attendees", methods=["GET"])
def get_attendees(event_id):
    try:
        attendee_handler = AttendeeHandler()
        http_request = HttpRequest(param={"event_id": event_id})

        http_response = attendee_handler.find_attendees_from_event(
            http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
