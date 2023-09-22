import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable = False, unique = True)
    user_name = Column(String(80), nullable = False, unique = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum, nullable = False)
    url = Column(String(250), nullable = False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1000), nullable = False)
    user_name = Column(String(80), nullable = False, unique = True)
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')