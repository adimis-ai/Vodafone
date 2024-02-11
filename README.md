# README

## Introduction
This documentation outlines the design, functionality, and usage of a Python script developed to address the requirements of SDE-1 Task 1, Ref. 22A in the domain of Data Science and Data Analytics. The script aims to construct a comprehensive database encompassing countries, their states, and corresponding capital cities. It provides functionality to perform various operations on the constructed database, such as retrieving countries with identical first and last letters, states with identical first and last letters, and cities with prime-length names.

## Script Overview
The script is structured into several classes and modules to ensure modularity, readability, and maintainability. Below is an overview of the main components:

1. **ORM (Object-Relational Mapping) Models**: Defined using SQLAlchemy, including `Country`, `State`, and `City`, representing the database schema for countries, states, and cities.

2. **Database Operations**: `DBOperations` class handles database interactions such as insertion of countries, states, and cities, retrieval of data, and specific queries like countries with identical first and last letters.

3. **ETL (Extract, Transform, Load) Pipeline**:
   - **Data Extractor**: `DataExtractor` class extracts data from provided CSV files containing information about countries, states, and cities.
   - **Data Transformer**: `DataTransformer` class transforms the extracted data into ORM model objects.
   - **Data Loader**: `DataLoader` class loads the transformed data into the database using `DBOperations`.

4. **ETL Driver**: `EtlDriver` class orchestrates the ETL process by utilizing the components mentioned above.

5. **CLI (Command-Line Interface) Driver**: `CliDriver` class provides a command-line interface for interacting with the database and performing operations like retrieving countries, states, and cities based on specific criteria.

## Functionality and Usage
The script offers the following functionality:

1. **Database Construction**: Upon execution, the script constructs a SQLite database containing tables for countries, states, and cities, along with necessary relationships.

2. **ETL Process**: The ETL process involves extracting data from provided CSV files, transforming it into ORM objects, and loading it into the database.

3. **CLI Interface**: Users can interact with the database through a command-line interface. They can select from various options:
   - Retrieve countries with identical first and last letters.
   - Retrieve states with identical first and last letters.
   - Retrieve cities with prime-length names.
   - Randomly choose one of the above options.

4. **Response Output**: Users have the option to save the response to a csv file for reference.

## Dependencies
The script relies on the following dependencies:
- Pandas: For data manipulation and CSV file handling.
- SQLAlchemy: For ORM functionality and database interaction.
- Click: For building command-line interfaces.
- Colorama: For colorizing command-line output.

## Execution Procedure

```bash
# Clone the repository
git clone https://github.com/adimis-ai/Vodafone.git
cd Vodafone

# Install dependencies
pip install -r requirements.txt

# Seed the database
python seed.py

# Execute the cli script
python run.py
```

## Conclusion
The provided Python script efficiently addresses the requirements of SDE-1 Task 1, Ref. 22A, by constructing a database of countries, states, and cities and offering a user-friendly CLI interface for interacting with the database.