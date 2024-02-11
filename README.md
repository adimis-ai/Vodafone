# Readme

## Sql Table Creation Query.

```sql
CREATE TABLE Country (
    country_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    first_letter CHAR(1) NOT NULL,
    last_letter CHAR(1) NOT NULL
);

CREATE TABLE State (
    state_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    first_letter CHAR(1) NOT NULL,
    last_letter CHAR(1) NOT NULL,
    is_capital_state BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (country_id) REFERENCES Country(country_id)
);

CREATE TABLE City (
    city_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    state_id INT NOT NULL,
    country_id INT NOT NULL,
    is_prime_length BOOLEAN NOT NULL,
    is_capital_city BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (state_id) REFERENCES State(state_id),
    FOREIGN KEY (country_id) REFERENCES Country(country_id)
);

-- Indexes
CREATE INDEX idx_country_name ON Country (name);
CREATE INDEX idx_country_first_letter ON Country (first_letter);
CREATE INDEX idx_country_last_letter ON Country (last_letter);
CREATE INDEX idx_state_name ON State (name);
CREATE INDEX idx_state_first_letter ON State (first_letter);
CREATE INDEX idx_state_last_letter ON State (last_letter);
CREATE INDEX idx_city_name ON City (name);
CREATE INDEX idx_city_prime_length ON City (is_prime_length);
CREATE INDEX idx_state_is_capital_state ON State (is_capital_state);
CREATE INDEX idx_city_is_capital_city ON City (is_capital_city);
```

## Project Structure

```

```
