# Este arquivo define a estrutura da tabela de eventos
from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

# Define a classe Events, que representa a tabela de eventos no banco de dados


class Events(Base):
    __tablename__ = "events"

    # Colunas da tabela de eventos
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)

    # Define a representação textual de um objeto Events quando ele é impresso
    def __repr__(self):
        return f"Events [title={self.title}, maximum_attendees={self.maximum_attendees}]"
