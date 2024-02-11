from typing import Tuple, List
from ..database.db_models import Country, City, State

class DataTransformer:
    def __init__(self, countries_df, states_df, cities_df):
        self.countries_df = countries_df
        self.states_df = states_df
        self.cities_df = cities_df
        self.transformed_countries = self._transform_countries()
        self.transformed_states = self._transform_states()
        self.transformed_cities = self._transform_cities()

    def _transform_countries(self):
        countries = []
        for _, row in self.countries_df.iterrows():
            country = Country(
                country_id=row['id'],
                name=row['name'],
                first_letter=row['name'][0].lower(),
                last_letter=row['name'][-1].lower()
            )
            countries.append(country)
        return countries

    def _transform_states(self):
        states = []
        for _, row in self.states_df.iterrows():
            state = State(
                state_id=row['id'],
                name=row['name'],
                country_id=row['country_id'],
                first_letter=row['name'][0].lower(),
                last_letter=row['name'][-1].lower(),
                is_capital_state=self._check_is_capital_state(row['country_id'], row['name'])
            )
            states.append(state)
        return states
    
    def _check_is_capital_state(self, country_id, state_name) -> bool:
        country_capital = self.countries_df.loc[self.countries_df['id'] == country_id, 'capital'].iloc[0]
        
        if isinstance(country_capital, str) and isinstance(state_name, str):
            # Check if state_name is a substring of country_capital or vice versa
            if state_name in country_capital or country_capital in state_name:
                return True
        
        return False

    def _transform_cities(self):
        cities = []
        for _, row in self.cities_df.iterrows():
            if isinstance(row['name'], str):
                city_name = row['name']
            else:
                city_name = "Unknown City"
            city = City(
                city_id=row['id'],
                name=city_name,
                state_id=row['state_id'],
                country_id=row['country_id']
            )
            cities.append(city)
        return cities
    
    def get_transformed_data(self) -> Tuple[List[Country], List[State], List[City]]:
        return self.transformed_countries, self.transformed_states, self.transformed_cities
