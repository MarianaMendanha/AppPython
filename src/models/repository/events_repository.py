from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound

# Esta classe fornece métodos para interagir com a tabela de eventos no banco de dados (Querys para banco)


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

    def count_event_attendees(self, event_id: str) -> Dict:
        # Início do bloco de código que gerencia a conexão com o banco de dados
        with db_connection_handler as database:
            # Consulta ao banco de dados para recuperar o número de participantes do evento com o ID fornecido
            event_count = (
                database.session
                # Inicia uma consulta para os registros da tabela Events
                .query(Events)
                # Realiza uma junção com a tabela Attendees usando a condição de igualdade entre os IDs dos eventos
                .join(Attendees, Events.id == Attendees.event_id)
                # Filtra os registros para incluir apenas aqueles com o ID do evento fornecido
                .filter(Events.id == event_id)
                # Define quais colunas devem ser retornadas na consulta
                .with_entities(
                    # Retorna o número máximo de participantes permitidos no evento
                    Events.maximum_attendees,
                    Attendees.id  # Retorna os IDs dos participantes
                )
                # Executa a consulta e retorna todos os resultados
                .all()
            )
            # Verifica se não há resultados na consulta (nenhum participante encontrado para o evento)
            if not len(event_count):
                # Retorna um dicionário indicando que não há participantes para o evento
                return {"maximumAttendees": 0, "attendeesAmount": 0}
            # Retorna um dicionário contendo o número máximo de participantes permitidos e a quantidade de participantes encontrados
            return {
                "maximumAttendees": event_count[0].maximum_attendees,
                "attendeesAmount": len(event_count)
            }
