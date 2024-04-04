from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError

# Esta classe fornece métodos para interagir com a tabela de check_ins no banco de dados


class CheckInsRepository:
    # Insere um novo check_in no banco de dados com as informações fornecidas
    def insert_check_in(self, attendee_id: str) -> str:
        # Estabelece uma conexão com o banco de dados
        with db_connection_handler as database:
            # Tratamento de erros
            try:
                # Cria um novo objeto CheckIns com as informações fornecidas
                check_in = (
                    CheckIns(attendeeId=attendee_id)
                )
                # Adiciona o check_in ao banco de dados e confirma a transação
                database.session.add(check_in)
                database.session.commit()

                # Retorna as informações do check_in inserido
                return attendee_id

            except IntegrityError:
                raise HttpConflictError('Checkin já foi feito!')

            except Exception as exception:
                database.session.rollback()
                raise exception
