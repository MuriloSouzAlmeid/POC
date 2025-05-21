from app.models import SQLModel, Field, datetime, create_engine, HTTPException
import uuid
from app.logging import logging
from app.config import settings

class NcmEntries(SQLModel, table=True):
    __tablename__ = "ncm_entries"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user: str
    ipi: str | None = Field(default=None)
    ncm: str
    description: str
    created_at : datetime

string_connection = settings.poc_stringconnection_database

try:
    engine = create_engine(string_connection)
except:
    logging.error("Ocorreu um erro ao conectar criar um engine com a string de conexao fornecida")
    raise HTTPException(status_code=500, detail="Falha ao conectar a aplicação com o banco de dados")


def create_tables():
    SQLModel.metadata.create_all(engine)