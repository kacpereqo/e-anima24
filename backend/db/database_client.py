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
    def get_user(self, session, username=None, email=None):
        if username is None and email is None:
            raise ValueError("Either username or email must be provided.")

        if username is None:
            username = email

        elif email is None:
            email = username

        user = (
            session.query(User)
            .filter(or_(User.username == username, User.email == email))
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
    def add_new_user(self, session, user, hashed_password):
        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password,
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
