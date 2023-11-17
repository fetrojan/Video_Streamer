from sqlalchemy import create_engine, Column, String, Date, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50))
    release_date = Column(Date)
    director = Column(String(50))


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_movie(title, genre, release_date, director):
    movie = Movie(title=title, genre=genre,
                  release_date=release_date, director=director)
    session.add(movie)
    session.commit()
    print(f"Filme '{movie.title}' adicionado com sucesso.")


def get_all_movies():
    return session.query(Movie).all()


def get_movie_by_title(title):
    return session.query(Movie).filter_by(title=title).first()


def delete_movie(title):
    movie = session.query(Movie).filter_by(title=title).first()
    if movie:
        session.delete(movie)
        session.commit()
        print(f"Movie '{title}' deleted successfully")
    else:
        print(f"Movie with title '{title}' not found.")
