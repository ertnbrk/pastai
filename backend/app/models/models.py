from sqlalchemy import Column, Integer, String, DateTime, JSON
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    created_at = Column(DateTime)

class Journal(Base):
    __tablename__ = 'journals'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    text = Column(String)
    date = Column(DateTime)

class Context(Base):
    __tablename__ = 'context'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    data = Column(JSON)
    updated_at = Column(DateTime)

class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    text = Column(String)
    datetime = Column(DateTime)