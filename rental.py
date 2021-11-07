import datetime
from enum import Enum
from movie import Movie, MovieCatalog

class PriceCode(Enum):
	"""An enumeration for different kinds of movies and their behavior"""
	new_release = { "price": lambda days: 3.0*days,
					"frp": lambda days: days
				  }
	regular = { "price": lambda days: 2 if days<=2 else 2 + 1.5*(days-2),
				"frp": lambda days: 1
			 }
	childrens = {"price": lambda days: 1.5 if days<=3 else 1.5 + 1.5*(days-3),
				 "frp": lambda days: 1
			    }

	def price(self, days: int) -> float:
            "Return the rental price for a given number of days"""
            pricing = self.value["price"]    # the enum member's price formula
            return pricing(days)

	def point(self, days: int) -> int:
		"Retrun the point for a given number of days"
		point = self.value["frp"]
		return point(days)

	@staticmethod
	def for_movie(movie: Movie):
		this_year = str(datetime.date.today().year)
		if movie.get_year() == this_year:
			return PriceCode.new_release
		elif movie.is_genre("Children"):
			return PriceCode.childrens
		else:
			return PriceCode.regular
		


class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""
	
	def __init__(self, movie, days_rented, price_code): 
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		if not isinstance(price_code, PriceCode):
			raise TypeError("movie must be Price code")
		self.movie = movie
		self.days_rented = days_rented
		self.price_code = price_code

	def get_title(self):
		return self.movie.get_title()

	def get_days_rented(self):
		return self.days_rented

	def get_charge(self):
		return self.price_code.price(self.days_rented)

	def get_rental_points(self):
		return self.price_code.point(self.days_rented)
