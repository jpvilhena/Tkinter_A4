from fastapi import FastAPI
from .database import engine, Base
from .routers import clients, trucks, drivers, helpers, services

app = FastAPI(title="MudaExpress API")


@app.on_event("startup")
def on_startup():
    # create tables if they don't exist
    Base.metadata.create_all(bind=engine)


app.include_router(clients.router)
app.include_router(trucks.router)
app.include_router(drivers.router)
app.include_router(helpers.router)
app.include_router(services.router)
