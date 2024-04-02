# Para testar: pytest -s -v src\models\repository\events_repository_test.py
import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

# Estabelece uma conexão com o banco de dados antes de executar os testes
db_connection_handler.connect_to_db()

# Método de teste para inserir um novo evento no banco de dados


@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_event():
    # Define um evento fictício para inserção
    event = {
        "uuid": "meu-uuid-outro",
        "title": "meu title",
        "slug": "meu-slug-2",
        "maximum_attendees": 20
    }

    # Instancia o repositório de eventos
    events_repository = EventsRepository()
    # Insere o evento no banco de dados e imprime a resposta
    response = events_repository.insert_event(event)
    print(response)

# Método de teste para obter um evento pelo seu ID


def test_get_event_by_id():
    # Define o ID do evento de teste
    test_event_id = "meu-uuid"

    # Instancia o repositório de eventos
    events_repository = EventsRepository()
    # Obtém o evento do banco de dados pelo seu ID e imprime a resposta e o título do evento
    response = events_repository.get_event_by_id(test_event_id)
    print(response)
    # print(response.title)
