import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.regular)
		self.childrens_movie = Movie("Frozen", PriceCode.childrens)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.regular)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.regular, m.get_price_code())

	# @unittest.skip("TODO add this test when you refactor rental price")
	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.get_price(), 3.5)
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.childrens_movie, 4)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.childrens_movie, 3)
		self.assertEqual(rental.get_price(), 1.5)

	# @unittest.skip("TODO add test of frequent renter points when you add it to Rental")
	def test_rental_points(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_point(), 1.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_point(), 5.0)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.get_point(), 1.0)
		rental = Rental(self.childrens_movie, 4)
		self.assertEqual(rental.get_point(), 1.0)
