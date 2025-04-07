from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import user
from app.infrastructure.database import create_db_and_tables


@asynccontextmanager
async def startup(app_: FastAPI):
    yield await create_db_and_tables()


app = FastAPI(
    title="Gogogo Ride-Sharing API",
    description="API for intercity ridesharing where drivers and passengers can connect.",
    version="1.0",
    contact={
        "name": "Elnazar Ulanbek uulu",
        "email": "elnazar.ulanbekuulu@outlook.com",
    },
    license_info={"name": "MIT License"},
    lifespan=startup
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api/users", tags=["Users"])


@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Welcome to Gogogo Ride-Sharing API 🚗"}
