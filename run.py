import colorama
from src.cli.cli import CliDriver

colorama.init()

if __name__ == "__main__":
    cli_driver = CliDriver()
    cli_driver.select_option()