import os

from dotenv import load_dotenv
from sqlalchemy import and_, create_engine, func, or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from .models import AnimeSeries, Base, Dislikes, Likes, User, Video


class DatabaseClient:
    def __init__(self):
        print("Initializing database client...")
        self.engine = self.create_engine()
        self.session_local = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        self.migrate()

    def connection(func):
        def wrapper(self, *args, **kwargs):
            session = self.session_local()
            try:
                return func(self, session, *args, **kwargs)
            finally:
                session.close()

        return wrapper

    def create_engine(self):
        load_dotenv()

        USERNAME = os.getenv("DB_USERNAME")
        PASSWORD = os.getenv("DB_PASSWORD")
        HOST = os.getenv("DB_HOST")
        DB_URI = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/neondb"

        engine = create_engine(DB_URI)

        return engine

    def migrate(self):
        Base.metadata.create_all(bind=self.engine)
        print("Migrated database successfully!")

    @connection
    def get_user_by_username(self, session, username):
        user = session.query(User).filter(User.username == username).first()
        return user

    @connection
    def get_user_by_email(self, session, email):
        user = session.query(User).filter(User.email == email).first()
        return user

    @connection
    def get_user_by_id(self, session, user_id):
        user = session.query(User).filter(User.user_id == user_id).first()
        return user

    @connection
    def get_user_by_email_or_username(self, session, email_or_username):
        user = (
            session.query(User)
            .filter(
                or_(User.email == email_or_username, User.username == email_or_username)
            )
            .first()
        )
        return user

    @connection
    def check_unique_credentials(self, session, username, email):
        user = (
            session.query(User)
            .filter(or_(User.username == username, User.email == email))
            .first()
        )

        return bool(user)

    @connection
    def add_new_user(self, session, user):
        if user.provider == "google":
            db_user = User(
                username=user.username,
                email=user.email,
                provider=user.provider,
                verifier=user.verifier,
                avatar=user.avatar,
            )

        if user.provider == "auth":
            db_user = User(
                username=user.username,
                email=user.email,
                provider=user.provider,
                verifier=user.verifier,
                avatar="https://www.zooplus.pl/magazyn/wp-content/uploads/2020/02/welsh-corgi-pembroke-768x512.jpeg",
            )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    @connection
    def add_anime_series(self, session, anime_series):
        try:
            session.add(anime_series)
            session.commit()
            session.refresh(anime_series)
        except IntegrityError:
            session.rollback()

    @connection
    def add_bulk_anime_series(self, session, anime_series):
        try:
            session.bulk_save_objects(anime_series)
            session.commit()
        except IntegrityError:
            session.rollback()
            print("IntegrityError")

    @connection
    def autocomplete_anime_series(self, session, query):
        anime_series = (
            session.query(AnimeSeries.name, AnimeSeries.anime_id)
            .filter(AnimeSeries.name.ilike(f"{query}%"))
            .limit(5)
            .all()
        )
        lst = [x[0] for x in anime_series]

        return lst

    @connection
    def add_anime(self, session, video):
        AnimeSeries_id = (
            session.query(AnimeSeries.anime_id)
            .filter(AnimeSeries.name == video.name)
            .first()
        )

        db_video = Video(
            video_url=video.video_url,
            season=video.season,
            episode=video.episode,
            user_id=video.user_id,
            group_id=video.group_id or None,
            AnimeSeries_id=AnimeSeries_id[0],
        )

        session.add(db_video)
        session.commit()

        # add likes and dislikes

        likes = Likes(user_id=video.user_id, video_id=db_video.video_id)
        dislikes = Dislikes(user_id=video.user_id, video_id=db_video.video_id)

        session.add(likes)
        session.add(dislikes)
        session.commit()

    @connection
    def get_anime(self, session, anime_id):
        # count dislikes and likes for anime

        anime = (
            session.query(
                Video,
                AnimeSeries,
                func.count(Likes.user_id),
                func.count(Dislikes.user_id),
            )
            .select_from(
                Video,
                Dislikes,
                Likes,
                AnimeSeries,
            )
            .filter(Video.video_id == anime_id)
            .join(AnimeSeries)
            .join(Dislikes)
            .join(Likes)
            .group_by(Video, AnimeSeries)
            .first()
        )

        result = {
            "likes": anime[2] - 1,
            "dislikes": anime[3] - 1,
            "views": anime.Video.views,
            "video_id": anime.Video.video_id,
            "video_url": anime.Video.video_url,
            "season": anime.Video.season,
            "episode": anime.Video.episode,
            "user_id": anime.Video.user_id,
            "group_id": anime.Video.group_id,
            "anime_id": anime.AnimeSeries.anime_id,
            "name": anime.AnimeSeries.name,
        }
        return result

    @connection
    def increment_views(self, session, anime_id):
        anime = session.query(Video).filter(Video.video_id == anime_id).first()
        anime.views += 1
        session.commit()
        return anime.views

    @connection
    def get_recent_videos(self, session, count: int):
        videos = (
            session.query(Video, AnimeSeries)
            .select_from(Video, AnimeSeries)
            .join(AnimeSeries)
            .order_by(Video.video_id.desc())
            .limit(count)
            .all()
        )

        result = []
        for video, anime in videos:
            result.append(
                {
                    "video_id": video.video_id,
                    "thumbnail": anime.medium_image,
                    "name": anime.name,
                }
            )

        return result
