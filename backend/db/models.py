from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    provider = Column(String)
    verifier = Column(String)
    avatar = Column(String)

    def __repr__(self):
        return f"""
        <User(
            user_id={self.user_id},
            username={self.username},
            email={self.email},
            provider={self.provider},
            verifier={self.verifier},
            avatar={self.avatar}
        )>
"""


class Video(Base):
    __tablename__ = "videos"

    video_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group_id = Column(Integer, nullable=True)
    season = Column(Integer)
    episode = Column(Integer)
    video_url = Column(String)
    views = Column(Integer, default=0)
    user_id = Column(Integer)

    AnimeSeries_id: Mapped[int] = mapped_column(ForeignKey("animeSeries.anime_id"))
    animeSeries = relationship("AnimeSeries", foreign_keys=[AnimeSeries_id])

    dislikes: Mapped[list["Dislikes"]] = relationship("Dislikes")
    likes: Mapped[list["Likes"]] = relationship("Likes")

    def __repr__(self):
        return f"""
        <Video(
            video_id={self.video_id},
            user_id={self.user_id},
            group_id={self.group_id},
            video_url={self.video_url},
        )>
"""


class AnimeSeries(Base):
    __tablename__ = "animeSeries"

    anime_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, autoincrement=True
    )
    name = Column(String)
    small_image = Column(String)
    medium_image = Column(String)
    large_image = Column(String)
    description = Column(String)
    short_description = Column(String)

    video: Mapped[list["Video"]] = relationship(back_populates="animeSeries")

    def __repr__(self):
        return f"""
        <Anime(
            anime_id={self.anime_id},
            anime_name={self.name},
            anime_description={self.description},
            anime_short_description={self.short_description}
        )>
"""


class Tag(Base):
    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return f"""
        <tags(
            tag_id={self.tag_id},
            tag_name={self.tag_name}
        )>
"""


class VideoTag(Base):
    __tablename__ = "videoTags"

    video_id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"""
        <VideoTag(
            video_tag_id={self.video_tag_id},
            video_id={self.video_id},
            tag_id={self.tag_id}
        )>
"""


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return f"""
        <groups(
            group_id={self.group_id},
            group_name={self.group_name}
        )>
"""


class Likes(Base):
    __tablename__ = "likes"

    user_id = Column(Integer, primary_key=True)
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.video_id"), primary_key=True
    )

    def __repr__(self):
        return f"""
        <likes(
            user_id={self.user_id},
            video_id={self.video_id}
        )>
"""


class Dislikes(Base):
    __tablename__ = "dislikes"

    user_id = Column(
        Integer,
        primary_key=True,
    )
    video_id: Mapped[int] = mapped_column(
        ForeignKey("videos.video_id"), primary_key=True
    )

    def __repr__(self):
        return f"""
        <dislikes(
            user_id={self.user_id},
            video_id={self.video_id}
        )>
"""
