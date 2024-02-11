import pandas

class DataExtractor:
    def __init__(self, countries_csv_path, states_csv_path, cities_csv_path):
        self.countries_df = pandas.read_csv(countries_csv_path)
        self.states_df = pandas.read_csv(states_csv_path)
        self.cities_df = pandas.read_csv(cities_csv_path)

    def get_df(self):
        return self.countries_df, self.states_df, self.cities_df
