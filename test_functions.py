from datetime import date
from main import add_movie, get_all_movies, get_movie_by_title, delete_movie

movie_data = {
    "title": "Inception",
    "genre": "Sci-Fi",
    "release_date": date(2000, 7, 16),
    "director": "Christopher Nolan",
}

add_movie(**movie_data)

all_movies = get_all_movies()
print("All Movies:")
for movie in all_movies:
    print(f"{movie.title} - {movie.genre}")


search_title = "Inception"
found_movie = get_movie_by_title(search_title)
if found_movie:
    print(f"Movie Found: {found_movie.title} - {found_movie.genre}")
else:
    print(f"Movie with title '{search_title}' not found.")


add_movie("The Dark Knight", "Action", date(2008, 7, 18), 'Christopher Nolan')

delete_movie(title)
