# Para testar: pytest -s -v src\models\repository\attendees_repository_test.py
import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

# Estabelece uma conexão com o banco de dados antes de executar os testes
db_connection_handler.connect_to_db()

# Método de teste para inserir um novo participante no banco de dados


@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_attendee():
    # Define um participante fictício para inserção
    event_id = "meu-uuid"
    attendees_info = {
        "uuid": "meu-uuid-attendee",
        "name": "meu name",
        "email": "meu-email-@mail.com",
        "event_id": event_id
    }

    # Instancia o repositório de participantes
    attendees_repository = AttendeesRepository()
    # Insere o participante no banco de dados e imprime a resposta
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

# Método de teste para obter um participante pelo seu ID


def test_get_attendee_badge_by_id():
    # Define o ID do participante de teste
    test_attendee_id = "meu-uuid-attendee"

    # Instancia o repositório de participantes
    attendees_repository = AttendeesRepository()
    # Obtém o participante do banco de dados pelo seu ID e imprime a resposta e o título do participante
    response = attendees_repository.get_attendee_badge_by_id(test_attendee_id)
    print(response)
    # print(response.title)
