from db.database import db
from fastapi import APIRouter
from videos.models import Video

router = APIRouter()


@router.post("/add")
async def add_anime(video: Video):
    return db.add_anime(video)


@router.get("/{anime_id}")
async def get_anime(anime_id: int):
    return db.get_anime(anime_id)


@router.get("/{anime_id}/views/add")
async def increment_views(anime_id: int):
    return db.increment_views(anime_id)


@router.get("/{anime_id}/like/{user_id}")
async def increment_likes(anime_id: int, user_id: int):
    return db.like_video(anime_id, user_id)


@router.get("/{anime_id}/dislike/{user_id}")
async def increment_dislikes(anime_id: int, user_id: int):
    return db.dislike_video(anime_id, user_id)


@router.get("/recent/{count}")
async def get_recent(count: int):
    return db.get_recent_videos(count)
