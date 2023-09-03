from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
        return f"<User(user_id={self.user_id}, username={self.username}, email={self.email}, provider={self.provider}, verifier={self.verifier})>"
