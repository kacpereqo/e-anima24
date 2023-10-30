from auth.rotues import router as auth_router
from autocomplete.routes import router as autocomplete_router
from fastapi import FastAPI
from migrations.routes import router as migrations_router
from videos.routes import router as videos_router


def import_routes(app: FastAPI):
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(migrations_router, prefix="/migrations", tags=["migrations"])
    app.include_router(
        autocomplete_router, prefix="/autocomplete", tags=["autocomplete"]
    )
    app.include_router(videos_router, prefix="/videos", tags=["videos"])
