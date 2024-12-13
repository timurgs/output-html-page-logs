"""Main factory builder of ``FastAPI`` server."""

from fastapi import FastAPI

from app.routes import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app
