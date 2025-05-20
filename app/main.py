from app import FastAPI
from app.routers import login, automation, results
from app.models import models
from app.models.models import create_tables

app = FastAPI()

app.include_router(login.router)
app.include_router(automation.router)
app.include_router(results.router)

if __name__ == "__main__":
    create_tables()

