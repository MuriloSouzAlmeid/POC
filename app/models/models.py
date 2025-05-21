from app.models import SQLModel, Field, datetime, create_engine, HTTPException
import uuid
from app.logging import logging

class NcmEntries(SQLModel, table=True):
    __tablename__ = "ncm_entries"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user: str
    ipi: str | None = Field(default=None)
    ncm: str
    description: str
    created_at : datetime

string_connection = "mssql+pyodbc://sa:Murilo12%24@NOTEBOOKFAMILIA/POC_Database?""driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"

try:
    engine = create_engine(string_connection)
except:
    logging.error("Ocorreu um erro ao conectar criar um engine com a string de conexao fornecida")
    raise HTTPException(status_code=500, detail="Falha ao conectar a aplicação com o banco de dados")


def create_tables():
    SQLModel.metadata.create_all(engine)