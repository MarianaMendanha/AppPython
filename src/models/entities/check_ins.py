# Este arquivo define a estrutura da tabela de check_ins
from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

# Define a classe Checkins, que representa a tabela de check_ins no banco de dados


class CheckIns(Base):
    __tablename__ = "check_ins"

    # Colunas da tabela de check_ins
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    attendeeId = Column(String, ForeignKey("attendees.id"), nullable=False)

    # Define a representação textual de um objeto Checkins quando ele é impresso
    def __repr__(self):
        return f"Checkins [created_at={self.created_at}, attendeeId={self.attendeeId}]"
