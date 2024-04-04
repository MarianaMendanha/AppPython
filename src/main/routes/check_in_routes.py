# Importação do módulo Blueprint da biblioteca Flask
from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler

# Criação de um Blueprint chamado "event_route" para as rotas relacionadas a eventos
check_in_route_bp = Blueprint("check_in_route", __name__)

# Definição da rota para lidar com requisições POST na raiz ("/events") do Blueprint "event_route"


@check_in_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_check_in(attendee_id):
    http_request = HttpRequest(param={"attendee_id":attendee_id})
    check_in_handler = CheckInHandler()
    http_response = check_in_handler.registry(http_request)

    return jsonify(http_response.body), http_response.status_code


# @check_in_route_bp.route("/check_ins/<event_id>", methods=["GET"])
# def get_check_in(event_id):
#     check_in_handler = CheckInHandler()
#     http_request = HttpRequest(param={"event_id": event_id})

#     http_response = check_in_handler.find_by_id(http_request)

#     return jsonify(http_response.body), http_response.status_code
