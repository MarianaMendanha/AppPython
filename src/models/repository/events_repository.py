from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound

# Esta classe fornece métodos para interagir com a tabela de eventos no banco de dados


class EventsRepository:
    # Insere um novo evento no banco de dados com as informações fornecidas
    def insert_event(self, eventsInfo: Dict) -> Dict:
        # Estabelece uma conexão com o banco de dados
        with db_connection_handler as database:
            # Tratamento de erros
            try:
                # Cria um novo objeto Events com as informações fornecidas
                event = Events(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees"),
                )
                # Adiciona o evento ao banco de dados e confirma a transação
                database.session.add(event)
                database.session.commit()

                # Retorna as informações do evento inserido
                return eventsInfo

            except IntegrityError:
                raise Exception('Evento ja cadastrado!')

            except Exception as exception:
                database.session.rollback()
                raise exception

    # Obtém um evento pelo seu ID
    def get_event_by_id(self, event_id: str) -> Events:
        # Estabelece uma conexão com o banco de dados
        with db_connection_handler as database:
            # Tratamento de erros
            try:
                # Consulta o banco de dados para obter o evento com o ID fornecido
                event = (
                    database.session
                    .query(Events)
                    .filter(Events.id == event_id)
                    .one()
                )
                # Retorna o evento encontrado
                return event

            except NoResultFound:
                return None
