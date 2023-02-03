from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

DNS = "postgresql+asyncpg://app:secret@127.0.0.1:5431/app"
engine = create_async_engine(DNS)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True)
    json = Column(JSON, nullable=False)







# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
#
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(64), unique=True, nullable=False)
#     password = Column(String(60), nullable=False)
#     creation_time = Column(DateTime, server_default=func.now())
#
#
# class Token(Base):
#     __tablename__ = "tokens"
#
#     id = Column(UUID, server_default=func.uuid_generate_v4(), primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
#     user = relationship("User", lazy="joined")
#     creation_time = Column(DateTime, server_default=func.now())
