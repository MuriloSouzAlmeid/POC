from app.models import SQLModel, Field, datetime, create_engine
import uuid

class NcmEntries(SQLModel, table=True):
    __tablename__ = "ncm_entries"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user: str
    ipi: str | None = Field(default=None)
    ncm: str
    description: str
    created_at : datetime

string_connection = "mssql+pyodbc://sa:Murilo12%24@NOTEBOOKFAMILIA/POC_Database?""driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"

engine = create_engine(string_connection, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)