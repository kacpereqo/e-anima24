import orjson
from db.database import db
from db.models import AnimeSeries
from fastapi import APIRouter
from starlette import status

router = APIRouter()


@router.get("/animeseries")
async def get_animeseries():
    with open("migrations/animeSeries.json", "rb") as f:
        animeseries = orjson.loads(f.read())["data"]
        animes = []

        for i, anime in enumerate(animeseries):
            animes.append(
                AnimeSeries(
                    name=anime["title"],
                    small_image=anime["thumbnail"],
                    medium_image=anime["picture"],
                    large_image="",
                    description="",
                    short_description="",
                )
            )

            if i % 50 == 0:
                db.add_bulk_anime_series(animes)
                animes = []
                print(f"Added {i} anime(s) to database successfully!")

    return status.HTTP_200_OK

    {
        "sources": [
            "https://anilist.co/anime/142051",
            "https://anime-planet.com/anime/raise-a-suilen-nvade-show",
            "https://kitsu.io/anime/47450",
            "https://myanimelist.net/anime/51478",
        ],
        "title": "!NVADE SHOW!",
        "type": "SPECIAL",
        "episodes": 1,
        "status": "FINISHED",
        "animeSeason": {"season": "FALL", "year": 2020},
        "picture": "https://cdn.myanimelist.net/images/anime/1930/122178.jpg",
        "thumbnail": "https://cdn.myanimelist.net/images/anime/1930/122178t.jpg",
        "synonyms": [
            "!nvade Show!",
            "Invade Show!",
            "RAISE A SUILEN",
            "RAISE A SUILEN: !NVADE SHOW!",
        ],
        "relations": [
            "https://anilist.co/anime/101633",
            "https://kitsu.io/anime/12330",
            "https://myanimelist.net/anime/37869",
        ],
        "tags": [
            "band",
            "full cgi",
            "music",
            "primarily female cast",
            "primarily teen cast",
        ],
    },
