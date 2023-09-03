import os

import uvicorn
from db.database import db
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from utils.config import import_routes


def get_app() -> FastAPI:
    app = FastAPI()
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    import_routes(app)
    app.add_middleware(
        SessionMiddleware, secret_key="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"
    )
    return app


app = get_app()


@app.on_event("startup")
async def startup_event():
    db.migrate()


if __name__ == "__main__":
    print("Starting server...")

    load_dotenv()
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8080"))
    debug = os.environ.get("DEBUG", True)

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        ssl_keyfile="./key.pem",
        ssl_certfile="./cert.pem",
    )
