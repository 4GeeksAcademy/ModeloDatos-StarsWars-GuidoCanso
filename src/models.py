import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from eralchemy2 import render_er
from src.models import Base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    subscription_date = Column(DateTime, default=datetime.utcnow)

    favorite_characters = relationship(
        "FavoriteCharacter", back_populates="user")
    favorite_planets = relationship("FavoritePlanet", back_populates="user")


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    population = Column(String(50))

    favorites = relationship("FavoritePlanet", back_populates="planet")


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(20))
    birth_year = Column(String(20))
    eye_color = Column(String(20))

    favorites = relationship("FavoriteCharacter", back_populates="character")


class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

    user = relationship("User", back_populates="favorite_planets")
    planet = relationship("Planet", back_populates="favorites")


class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)

    user = relationship("User", back_populates="favorite_characters")
    character = relationship("Character", back_populates="favorites")


render_er(Base, 'diagram.png')
