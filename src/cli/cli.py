import pandas
import click
import random
import colorama
from ..database.db_operations import DBOperations

colorama.init()

class CliDriver:
    def __init__(self):
        self.db = DBOperations()

    def select_option(self):
        click.echo("Select an option:")
        click.echo("1. Countries with identical first and last letters")
        click.echo("2. States with identical first and last letters")
        click.echo("3. Cities with prime length names")
        click.echo("4. Randomly pick one option")
        filename = ''
        save_response = click.prompt("Do you want to save the response in a CSV file? (y/n)", type=str)
        if save_response.lower() == 'y':
            filename = click.prompt("Enter filename to save the response", type=str)
            save_to_file = True
        else:
            save_to_file = False

        option = click.prompt("Enter option number", type=int)

        if option == 1:
            self._countries_with_identical_first_and_last_letters(save_to_file, filename)
        elif option == 2:
            self._states_with_identical_first_and_last_letters(save_to_file, filename)
        elif option == 3:
            self._cities_with_prime_length_names(save_to_file, filename)
        elif option == 4:
            self._randomly_pick_option(save_to_file, filename)
        else:
            click.echo(colorama.Fore.RED + "Invalid option")

    def _countries_with_identical_first_and_last_letters(self, save_to_file: bool, filename: str):
        result = self.db.countries_with_identical_first_and_last_letters()
        self._save_result_to_csv(result, 1, save_to_file, filename)

    def _states_with_identical_first_and_last_letters(self, save_to_file: bool, filename: str):
        result = self.db.states_with_identical_first_and_last_letters()
        self._save_result_to_csv(result, 2, save_to_file, filename)

    def _cities_with_prime_length_names(self, save_to_file: bool, filename: str):
        result = self.db.cities_with_prime_length_names()
        self._save_result_to_csv(result, 3, save_to_file, filename)

    def _randomly_pick_option(self, save_to_file: bool, filename: str):
        options = [
            self._cities_with_prime_length_names,
            self._countries_with_identical_first_and_last_letters,
            self._states_with_identical_first_and_last_letters,
        ]
        random.choice(options)(save_to_file, filename)

    def _save_result_to_csv(self, result, option: int, save_to_file: bool, filename: str):
        if save_to_file:
            if option == 1:
                df = pandas.DataFrame(result, columns=['Country'])
            elif option == 2:
                df = pandas.DataFrame(result, columns=['Country', 'State'])
            else:
                df = pandas.DataFrame(result, columns=['City', 'Country'])
            df.to_csv(f"{filename}.csv", index=True)
            click.echo(colorama.Fore.GREEN + f"Data saved to {filename}.csv")
        else:
            click.echo(colorama.Fore.GREEN + "\n".join(result))
