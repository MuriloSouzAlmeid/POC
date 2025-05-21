from app import FastAPI, get_openapi
from app.routers import login, automation, results
from app.models import models
from app.models.models import create_tables

app = FastAPI()

app.include_router(login.router)
app.include_router(automation.router)
app.include_router(results.router)

if __name__ == "__main__":
    create_tables()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="POC - Desafio DevCertacon",
        version="1.0",
        summary="O projeto POC é uma prova de conceito que integra automação web com Selenium e uma API construída em FastAPI, com persistência de dados em Microsoft SQL Server usando o SQLModel e exportação de dados para um arquivo de planilhas Excel usando Openpyxl.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

