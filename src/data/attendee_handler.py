import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class AttendeeHandler:
    def __init__(self) -> None:
        # Initialize the AttendeesRepository object
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        # Get the request body
        body = http_request.body
        event_id = http_request.param["event_id"]

        # Não podemos cadastrar se já alcançou o limite de participantes
        event_attendees_count = self.__events_repository.count_event_attendees(
            event_id)
        if (event_attendees_count["attendeesAmount"] and
                event_attendees_count["maximumAttendees"] < event_attendees_count["attendeesAmount"]):
            raise Exception("Evento lotado")

        # Generate a unique UUID for the attendee
        body["uuid"] = str(uuid.uuid4())
        print("Olha aqui o uuid>>", body["uuid"])
        body["event_id"] = event_id

        # If there is no body or it's empty we return a bad request response
        if not body:
            return HttpResponse(400, "Corpo da requisição vazio ou inválido.")

        # Insert the event into the repository
        self.__attendees_repository.insert_attendee(body)

        # Return a response with the generated UUID
        return HttpResponse(
            body=None,
            status_code=201
        )

    def find_attendee_badge(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param["attendee_id"]
        badge = self.__attendees_repository.get_attendee_badge_by_id(
            attendee_id)
        if not badge:
            raise Exception('Participante não encontrado')

        return HttpResponse(
            body={
                "badge": {
                    "name": badge.name,
                    "email": badge.email,
                    "eventTitle": badge.title
                }
            },
            status_code=200
        )

    def find_attendees_from_event(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        attendees = self.__attendees_repository.get_attendees_by_event_id(
            event_id)
        if not attendees:
            raise Exception('Não há participantes')

        formatted_attendees = []
        for attendee in attendees:
            formatted_attendees.append(
                {
                    "id": attendee.id,
                    "name": attendee.name,
                    "email": attendee.email,
                    "checkedInAtt": attendee.checkedInAt,
                    "createdAt": attendee.createdAt
                }
            )

        return HttpResponse(
            body={"attendees": formatted_attendees},
            status_code=200
        )
