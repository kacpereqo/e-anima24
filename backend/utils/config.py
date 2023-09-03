from auth.rotues import router

# from auth.test import router
from fastapi import FastAPI


def import_routes(app: FastAPI):
    app.include_router(router, prefix="/auth", tags=["auth"])
