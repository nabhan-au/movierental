import re
import unittest 
from customer import Customer
from rental import Rental, PriceCode
from movie import MovieCatalog

class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
	
	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.catalog = MovieCatalog()
		self.c = Customer("Movie Mogul")
		self.regular_movie = "Steve Jobs"
		self.childrens_movie = "Frozen"
		
	@unittest.skip("No convenient way to test")
	def test_billing():
		# no convenient way to test billing since its buried in the statement() method.
		pass
	
	def test_statement(self):
		stmt = self.c.statement()
		# visual testing
		print(stmt)
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		movie = self.catalog.get_movie(self.regular_movie)
		self.c.add_rental(Rental(movie, 4, PriceCode.for_movie(movie))) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("5.00", matches[1])
