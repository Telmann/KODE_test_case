from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    notes = relationship('Note', back_populates='user')


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='notes')
