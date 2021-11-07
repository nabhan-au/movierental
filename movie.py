from typing import Dict, List
import csv

class Movie:
	"""
	A movie available for rent.
	"""
	def __init__(self, title, year, genre):
		# Initialize a new movie.
		self._title = title
		self._year = year
		self._genre = genre
	
	def get_title(self):
		return self._title

	def get_year(self):
		return self._year

	def get_genre(self):
		return self._genre

	def is_genre(self, genre):
		return genre in self._genre


class MovieCatalog:

	def __init__(self) -> None:
		self._movies_dict: Dict[str, Movie]  = {}

	def get_movie(self, movie_name):
		self.__read_file(movie_name)
		return self._movies_dict[movie_name]

	def __read_file(self, movie_name):
		#check if movie in movie dict or not. If not find it in csv file and add to dict
		if movie_name not in self._movies_dict:
			#open movie file
			file = open('movies.csv')
			movie_catalog = csv.reader(file)
			for movie in movie_catalog:
				if movie[1] == movie_name:
					year = movie[2]
					genre = movie[3].split('|')
					self._movies_dict[movie_name] = Movie(movie_name, year, genre)
					break
