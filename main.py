# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import MovieCatalog
from rental import PriceCode, Rental
from customer import Customer

if __name__ == '__main__':
    # Create movie catalog
    catalog = MovieCatalog()
    #List of movie name
    movie_name = ["Fifty Shades of Grey", "The Martian", "Mulan", "Jurassic World", "Particle Fever"]
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for title in movie_name:
        # Get movie
        movie = catalog.get_movie(title)
        # Add movie to user rent list
        customer.add_rental(Rental(movie, days, PriceCode.for_movie(movie)))
        days += 1
    print(customer.statement())
