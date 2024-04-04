from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.check_ins import CheckIns
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError

# Esta classe fornece métodos para interagir com a tabela de participantes no banco de dados (Querys)


class AttendeesRepository:
    # Insere um novo participante no banco de dados com as informações fornecidas
    def insert_attendee(self, attendee_info: Dict) -> Dict:
        # Estabelece uma conexão com o banco de dados
        with db_connection_handler as database:
            # Tratamento de erros
            try:
                # Cria um novo objeto Attendees com as informações fornecidas
                attendee = (
                    Attendees(
                        id=attendee_info.get("uuid"),
                        name=attendee_info.get("name"),
                        email=attendee_info.get("email"),
                        event_id=attendee_info.get("event_id")
                    )
                )
                # Adiciona o participante ao banco de dados e confirma a transação
                database.session.add(attendee)
                database.session.commit()

                # Retorna as informações do participante inserido
                return attendee_info

            except IntegrityError:
                raise HttpConflictError('Participante ja cadastrado!')

            except Exception as exception:
                database.session.rollback()
                raise exception

    # Obtém um participante pelo seu ID
    def get_attendee_badge_by_id(self, attendee_id: str):
        # Estabelece uma conexão com o banco de dados
        with db_connection_handler as database:
            # Tratamento de erros
            try:
                # Consulta o banco de dados para obter o participante com o ID fornecido
                attendee = (
                    database.session
                    .query(Attendees)
                    .join(Events, Events.id == Attendees.event_id)
                    .filter(Attendees.id == attendee_id)
                    .with_entities(
                        Attendees.name,
                        Attendees.email,
                        Events.title,
                    )
                    .one()
                )
                # Retorna o participante encontrado
                return attendee

            except NoResultFound:
                return None

    def get_attendees_by_event_id(self, event_id: str) -> List[Attendees]:
        """Retorna todos os participantes de um determinado evento."""
        with db_connection_handler as database:
            attendees = (
                database.session
                .query(Attendees)
                .outerjoin(CheckIns, CheckIns.attendeeId == Attendees.id)
                .filter(Attendees.event_id == event_id)
                .with_entities(
                    Attendees.id,
                    Attendees.name,
                    Attendees.email,
                    CheckIns.created_at.label('checkedInAt'),
                    Attendees.created_at.label('createdAt')
                )
                .all()
            )
            return attendees