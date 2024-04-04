import uuid
from src.models.repository.check_ins_repository import CheckInsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class CheckInHandler:
    def __init__(self) -> None:
        # Initialize the CheckInsRepository object
        self.__check_ins_repository = CheckInsRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        check_in_infos = http_request.param["attendee_id"]

        # Insert the checkin into the repository
        self.__check_ins_repository.insert_check_in(check_in_infos)

        # Return a response with check_in_infos
        return HttpResponse(
            body=None,
            status_code=201
        )

    # def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
    #     event_id = http_request.param["event_id"]
    #     event = self.__events_repository.get_event_by_id(event_id)
    #     if not event:
    #         raise Exception('Evento não encontrado')

    #     event_attendees_count = self.__events_repository.count_event_attendees(
    #         event_id)

    #     return HttpResponse(
    #         body={
    #             "event": {
    #                 "id": event.id,
    #                 "title": event.title,
    #                 "details": event.details,
    #                 "slug": event.slug,
    #                 "maximumAttendees": event.maximum_attendees,
    #                 "attendeesAmount": event_attendees_count["attendeesAmount"]
    #             }
    #         },
    #         status_code=200
    #     )
