from .db_connector import DBConnector
from .db_models import Country, State, City
from sqlalchemy import func
from typing import List
from ..config.config import Config
import json

class DBOperations:
    def __init__(self):
        self.config = Config()
        self.db_connector: DBConnector = DBConnector(self.config.DB_NAME)

    def insert_country(self, name, first_letter, last_letter):
        country = Country(name=name, first_letter=first_letter, last_letter=last_letter)
        self.db_connector.session.add(country)
        self.db_connector.session.commit()
        print(f"Added country: {country}")

    def insert_state(self, name, country_id, first_letter, last_letter, is_capital_state=False):
        state = State(name=name, country_id=country_id, first_letter=first_letter,
                        last_letter=last_letter, is_capital_state=is_capital_state)
        self.db_connector.session.add(state)
        self.db_connector.session.commit()
        print(f"Added state: {state}")

    def insert_city(self, name, state_id, country_id):
        city = City(name=name, state_id=state_id, country_id=country_id)
        self.db_connector.session.add(city)
        self.db_connector.session.commit()
        print(f"Added city: {city}")

    def insert_countries_bulk(self, countries_data: List[tuple]):
        countries = [Country(name=name, first_letter=first_letter, last_letter=last_letter) for name, first_letter, last_letter in countries_data]
        self.db_connector.session.add_all(countries)
        self.db_connector.session.commit()
        print("Added countries in bulk.")

    def insert_states_bulk(self, states_data: List[tuple]):
        states = [State(name=name, country_id=country_id, first_letter=first_letter, last_letter=last_letter, is_capital_state=is_capital_state) for name, country_id, first_letter, last_letter, is_capital_state in states_data]
        self.db_connector.session.add_all(states)
        self.db_connector.session.commit()
        print("Added states in bulk.")

    def insert_cities_bulk(self, cities_data: List[tuple]):
        cities = [City(name=name, state_id=state_id, country_id=country_id) for name, state_id, country_id in cities_data]
        self.db_connector.session.add_all(cities)
        self.db_connector.session.commit()
        print("Added cities in bulk.")

    def get_all_countries(self):
        return self.db_connector.session.query(Country).all()

    def get_all_states(self):
        return self.db_connector.session.query(State).all()

    def get_all_cities(self):
        return self.db_connector.session.query(City).all()

    def countries_with_identical_first_and_last_letters(self):
        countries = self.db_connector.session.query(Country.name).filter(Country.first_letter == Country.last_letter).all()
        return countries

    def states_with_identical_first_and_last_letters(self):
        return self.db_connector.session.query(Country.name, State.name).\
            join(State, State.country_id == Country.country_id).\
            filter(State.first_letter == State.last_letter).all()

    def cities_with_prime_length_names(self):
        return self.db_connector.session.query(City.name, Country.name).\
            join(Country, City.country_id == Country.country_id).\
            filter(func.LENGTH(City.name).in_([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])).all()

# if __name__ == "__main__":
#     db_connector = DBConnector("example2.db")
#     db_operations = DBOperations(db_connector)

#     # Inserting countries
#     countries_data = [
#         ('United States', 'u', 's'),
#         ('Canada', 'c', 'a'),
#         ('Brazil', 'b', 'l'),
#         ('Germany', 'g', 'y'),
#         ('Japan', 'j', 'n'),
#         ('India', 'i', 'a'),
#         ('Australia', 'a', 'a'),
#         ('France', 'f', 'e'),
#         ('United Kingdom', 'u', 'd'),
#         ('Italy', 'i', 'y')
#     ]
#     db_operations.insert_countries_bulk(countries_data)

#     # Inserting states
#     states_data = [
#         ('New York', 1, 'n', 'k', True),
#         ('California', 1, 'c', 'a', False),
#         ('Ontario', 2, 'o', 'o', False),
#         ('São Paulo', 3, 's', 'o', True),
#         ('Berlin', 4, 'b', 'n', True),
#         ('Tokyo', 5, 't', 'o', True),
#         ('Maharashtra', 6, 'm', 'a', False),
#         ('New South Wales', 7, 'n', 's', False),
#         ('Île-de-France', 8, 'î', 'e', True),
#         ('England', 9, 'e', 'd', False)
#     ]
#     db_operations.insert_states_bulk(states_data)

#     # Inserting cities
#     cities_data = [
#         ('New York City', 1, 1),
#         ('Los Angeles', 2, 1),
#         ('Toronto', 3, 2),
#         ('São Paulo', 4, 3),
#         ('Berlin', 5, 4),
#         ('Tokyo', 6, 5),
#         ('Mumbai', 7, 6),
#         ('Sydney', 8, 7),
#         ('Paris', 9, 8),
#         ('London', 10, 9)
#     ]
#     db_operations.insert_cities_bulk(cities_data)

#     print("All Countries:")
#     for country in db_operations.get_all_countries():
#         print(country)

#     print("\nAll States:")
#     for state in db_operations.get_all_states():
#         print(state)

#     print("\nAll Cities:")
#     for city in db_operations.get_all_cities():
#         print(city)
    
#     countries_with_identical_first_and_last_letter = db_operations.countries_with_identical_first_and_last_letters()
#     print("\nCountries with identical first and last letters:")
#     for country in countries_with_identical_first_and_last_letter:
#         print(country)

#     states_with_identical_first_and_last_letter = db_operations.states_with_identical_first_and_last_letters()
#     print("\nStates with identical first and last letters:")
#     for state in states_with_identical_first_and_last_letter:
#         print(state)

#     cities_with_prime_length_names = db_operations.cities_with_prime_length_names()
#     print("\nCities with prime length names:")
#     for city in cities_with_prime_length_names:
#         print(city)

#     db_connector.close_connection()
