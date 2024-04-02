# Arquivo que faz a conexão com o banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class __DBConnectionHandler:
    def __init__(self) -> None:
        # Configura a string de conexão com o banco de dados SQLite
        self.__connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        )
        self.__engine = None

    def connect_to_db(self) -> None:
        # Cria uma instância de motor de banco de dados SQLAlchemy
        self.__engine = create_engine(self.__connection_string)
        self.session = None

    def get_engine(self):
        # Retorna o objeto do motor de banco de dados
        return self.__engine

    def __enter__(self):
        print('Estou entrando')
        # Quando a instância é usada com a instrução "with", inicia uma sessão
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_typr, exc_val, exc_tb):
        print('Estou saindo')
        # Quando a instância é usada com a instrução "with", fecha a sessão ao sair


db_connection_handler = __DBConnectionHandler()
