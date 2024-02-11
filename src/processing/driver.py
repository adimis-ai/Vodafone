from ..database.db_connector import DBConnector
from ..database.db_operations import DBOperations
from .extractor import DataExtractor
from .transformer import DataTransformer
from .loader import DataLoader

class EtlDriver:
    def __init__(self, countries_name, states_name, cities_name):
        self.db_operations = DBOperations()
        self.extractor = DataExtractor(countries_name=countries_name, states_name=states_name, cities_name=cities_name)
        self.countries_df, self.states_df, self.cities_df = self.extractor.get_df()
        self.transformer = DataTransformer(self.countries_df, self.states_df, self.cities_df)
        self.transformed_countries, self.transformed_states, self.transformed_cities = self.transformer.get_transformed_data()
        self.data_loader = DataLoader(self.db_operations)

    def run_etl_process(self):
        self.data_loader.load_transformed_countries(self.transformed_countries)
        self.data_loader.load_transformed_states(self.transformed_states)
        self.data_loader.load_transformed_cities(self.transformed_cities)