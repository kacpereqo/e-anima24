from pydantic import BaseModel


class Video(BaseModel):
    name: str
    video_url: str
    season: int
    episode: int
    user_id: int
    group_id: int | None = None
