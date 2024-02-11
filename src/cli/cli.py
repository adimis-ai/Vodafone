import click
import random
import colorama
from ..database.db_operations import DBOperations
from ..utils.save_data import save_file

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
        save_response = click.prompt("Do you want to save the response in a text file? (y/n)", type=str)
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
        countries_data = self._format_result(result, "Countries with Identical First and Last Letters:")
        self._save_or_print_result(countries_data, save_to_file, filename)

    def _states_with_identical_first_and_last_letters(self, save_to_file: bool, filename: str):
        result = self.db.states_with_identical_first_and_last_letters()
        states_and_countries = self._format_result(result, "States with Identical First and Last Letters:")
        self._save_or_print_result(states_and_countries, save_to_file, filename)

    def _cities_with_prime_length_names(self, save_to_file: bool, filename: str):
        result = self.db.cities_with_prime_length_names()
        cities = self._format_result(result, "Cities with Prime Length Names:")
        self._save_or_print_result(cities, save_to_file, filename)

    def _randomly_pick_option(self, save_to_file: bool, filename: str):
        options = [
            self._cities_with_prime_length_names,
            self._countries_with_identical_first_and_last_letters,
            self._states_with_identical_first_and_last_letters,
        ]
        random.choice(options)(save_to_file, filename)

    def _format_result(self, result, message):
        formatted_data = []
        click.echo(colorama.Fore.GREEN + message)
        for item in result:
            formatted_data.append(self._format_item(item))
        return formatted_data

    def _format_item(self, item):
        if len(item) == 1:
            return item[0]
        else:
            return ', '.join(item)

    def _save_or_print_result(self, data, save_to_file: bool, filename: str):
        if save_to_file:
            save_file(filename, '\n'.join(data))
            click.echo(colorama.Fore.GREEN + f"Data saved to {filename}")
        else:
            click.echo(colorama.Fore.GREEN + "\n".join(data))
