from typing import List
from ..database.db_operations import DBOperations
from ..database.db_models import Country, State, City

class DataLoader:
    def __init__(self, db_operations: DBOperations):
        self.db_operations = db_operations

    def load_transformed_countries(self, transformed_countries: List[Country]):
        countries_data = [(country.name, country.first_letter, country.last_letter) for country in transformed_countries]
        self.db_operations.insert_countries_bulk(countries_data)

    def load_transformed_states(self, transformed_states: List[State]):
        states_data = [(state.name, state.country_id, state.first_letter, state.last_letter, state.is_capital_state) for state in transformed_states]
        self.db_operations.insert_states_bulk(states_data)

    def load_transformed_cities(self, transformed_cities: List[City]):
        cities_data = [(city.name, city.state_id, city.country_id) for city in transformed_cities]
        self.db_operations.insert_cities_bulk(cities_data)