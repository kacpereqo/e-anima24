import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from .models import Base, User


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
        db_user = User(
            username=user.username,
            email=user.email,
            provider=user.provider,
            verifier=user.verifier,
            avatar=user.avatar,
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
