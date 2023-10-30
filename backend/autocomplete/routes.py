from db.database import db
from fastapi import APIRouter

router = APIRouter()


@router.get("/series")
async def get_series_autocomplete(query: str):
    return db.autocomplete_anime_series(query)
