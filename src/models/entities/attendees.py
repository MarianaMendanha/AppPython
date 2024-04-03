# Este arquivo define a estrutura da tabela de participantes
from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

# Define a classe Attendees, que representa a tabela de participantes no banco de dados


class Attendees(Base):
    __tablename__ = "attendees"

    # Colunas da tabela de participantes
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey("events.id"))
    created_at = Column(DateTime, default=func.now())

    # Define a representação textual de um objeto Attendees quando ele é impresso
    def __repr__(self):
        return f"Attendees [name={self.name}, event_id={self.event_id}, email={self.email}]"
