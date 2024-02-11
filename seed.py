import colorama
from src.processing.driver import EtlDriver

colorama.init()

if __name__ == "__main__":
    print(colorama.Fore.BLUE + "Seeding Database")
    etl_driver = EtlDriver(
        countries_name="countries.csv",
        states_name="states.csv",
        cities_name="cities.csv"
    )
    etl_driver.run_etl_process()
    print(colorama.Fore.BLUE + "Seeding Completed, you can now run `python run.py`")
    print(colorama.Fore.BLUE + "Bye...")
    print(colorama.Style.RESET_ALL)