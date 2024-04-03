import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class EventHandler:
    def __init__(self) -> None:
        # Initialize the EventsRepository object
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        # Get the request body
        body = http_request.body

        # Generate a unique UUID for the event
        body["uuid"] = str(uuid.uuid4())
        print("Olha aqui o uuid>>", body["uuid"])

        # Insert the event into the repository
        self.__events_repository.insert_event(body)

        # Return a response with the generated UUID
        return HttpResponse(
            body={"eventId": body["uuid"]},
            status_code=200
        )

    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event = self.__events_repository.get_event_by_id(event_id)
        if not event:
            raise Exception('Evento não encontrado')

        event_attendees_count = self.__events_repository.count_event_attendees(
            event_id)

        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximumAttendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_count["attendeesAmount"]
                }
            },
            status_code=200
        )
