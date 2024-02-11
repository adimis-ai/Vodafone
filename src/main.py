import colorama
from .cli.cli import CliDriver
from .processing.driver import EtlDriver

colorama.init()

def main():
    print(colorama.Fore.BLUE + "Loading Data...")
    etl_driver = EtlDriver(
        countries_csv_path=r"C:\Users\adimi\Documents\Adimis\Assignments\Vodafone\src\data\countries.csv",
        states_csv_path=r"C:\Users\adimi\Documents\Adimis\Assignments\Vodafone\src\data\states.csv",
        cities_csv_path=r"C:\Users\adimi\Documents\Adimis\Assignments\Vodafone\src\data\cities.csv"
    )
    etl_driver.run_etl_process()
    print(colorama.Fore.BLUE + "Data Loaded...")
    print(colorama.Style.RESET_ALL)
    cli_driver = CliDriver()
    cli_driver.select_option()
