import os
import pandas

class DataExtractor:
    def __init__(self, countries_name, states_name, cities_name):
        countries_csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', countries_name))
        states_csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', states_name))
        cities_csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', cities_name))
        self.countries_df = pandas.read_csv(countries_csv_path)
        self.states_df = pandas.read_csv(states_csv_path)
        self.cities_df = pandas.read_csv(cities_csv_path)

    def get_df(self):
        return self.countries_df, self.states_df, self.cities_df
