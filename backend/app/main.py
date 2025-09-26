from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api_router


def get_app() -> FastAPI:
    app = FastAPI(
        title="Passport Recognition API",
        description="Extract passport data from MRZ (Machine Readable Zone)",
        version="1.0.0",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")

    return app

app = get_app()
