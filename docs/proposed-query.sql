-- SECTION: Country Table
CREATE TABLE Country (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    first_letter CHAR(1) NOT NULL CHECK (first_letter = LOWER(first_letter)),
    last_letter CHAR(1) NOT NULL CHECK (last_letter = LOWER(last_letter))
);
-- Composite Indexes
CREATE INDEX idx_country_first_last_letter ON Country (first_letter, last_letter);

-- SECTION: State Table
CREATE TABLE State (
    state_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    first_letter CHAR(1) NOT NULL CHECK (first_letter = LOWER(first_letter)),
    last_letter CHAR(1) NOT NULL CHECK (last_letter = LOWER(last_letter)),
    is_capital_state BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (country_id) REFERENCES Country(country_id)
);
-- Composite Indexes
CREATE INDEX idx_state_first_last_letter ON State (first_letter, last_letter);

-- SECTION: City Table
CREATE TABLE City (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    state_id INT NOT NULL,
    country_id INT NOT NULL,
    is_capital_city BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (state_id) REFERENCES State(state_id),
    FOREIGN KEY (country_id) REFERENCES Country(country_id)
);
-- Composite Indexes
CREATE INDEX idx_city_name ON City (name);
CREATE INDEX idx_city_is_capital_city ON City (is_capital_city);

-- SECTION: Insert Data
INSERT INTO Country (name, first_letter, last_letter) VALUES
('United States', 'u', 's'),
('Canada', 'c', 'a'),
('Brazil', 'b', 'l'),
('Germany', 'g', 'y'),
('Japan', 'j', 'n'),
('India', 'i', 'a'),
('Australia', 'a', 'a'),
('France', 'f', 'e'),
('United Kingdom', 'u', 'd'),
('Italy', 'i', 'y');

INSERT INTO State (name, country_id, first_letter, last_letter, is_capital_state) VALUES
('New York', 1, 'n', 'k', TRUE),
('California', 1, 'c', 'a', FALSE),
('Ontario', 2, 'o', 'o', FALSE),
('São Paulo', 3, 's', 'o', TRUE),
('Berlin', 4, 'b', 'n', TRUE),
('Tokyo', 5, 't', 'o', TRUE),
('Maharashtra', 6, 'm', 'a', FALSE),
('New South Wales', 7, 'n', 's', FALSE),
('Île-de-France', 8, 'î', 'e', TRUE),
('England', 9, 'e', 'd', FALSE);

INSERT INTO City (name, state_id, country_id, is_capital_city) VALUES
('New York City', 1, 1, TRUE),
('Los Angeles', 2, 1, FALSE),
('Toronto', 3, 2, FALSE),
('São Paulo', 4, 3, TRUE),
('Berlin', 5, 4, TRUE),
('Tokyo', 6, 5, TRUE),
('Mumbai', 7, 6, FALSE),
('Sydney', 8, 7, TRUE),
('Paris', 9, 8, TRUE),
('London', 10, 9, TRUE);

-- SECTION: User Inputs Queries
-- A: Countries with Identical First and Last Letters: List all countries whose names start and end with the same alphabet
-- Example: India, Indonesia, Australia, Argentina. Note: India and Indonesia start with 'I' and end with 'a
SELECT name 
FROM Country 
WHERE first_letter = last_letter;

-- W: States with Identical First and Last Letters: Display all countries and their states where the state names begin and end with the same alphabet.
-- Example: In the USA, "Alabama" and "Alaska" are two states where the state names meet the criteria.
SELECT c.name AS country_name, s.name AS state_name
FROM Country c
JOIN State s ON s.country_id = c.country_id
WHERE s.first_letter = s.last_letter;

-- D: Cities with Prime-Length Names: Provide a list of cities from countries whose city names have a prime number of characters.
-- Example: "Paris" (France), "Rome" (Italy), and "Berlin" (Germany) have prime-length city names.
SELECT ci.name AS city_name, co.name AS country_name
FROM City ci
JOIN Country co ON ci.country_id = co.country_id
WHERE LENGTH(ci.name) IN (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
