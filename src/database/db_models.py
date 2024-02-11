from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    first_letter = Column(String(1), nullable=False)
    last_letter = Column(String(1), nullable=False)

    states = relationship('State', back_populates='country')

    def __repr__(self) -> str:
        return f"Country(country_id={self.country_id!r}, name={self.name!r})"

class State(Base):
    __tablename__ = 'state'

    state_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
    first_letter = Column(String(1), nullable=False)
    last_letter = Column(String(1), nullable=False)
    is_capital_state = Column(Boolean, nullable=False, default=False)

    country = relationship('Country', back_populates='states')
    cities = relationship('City', back_populates='state')

    def __repr__(self) -> str:
        return f"State(state_id={self.state_id!r}, name={self.name!r})"

class City(Base):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    state_id = Column(Integer, ForeignKey('state.state_id'), nullable=False)
    country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
    is_prime_length = Column(Boolean, nullable=False)
    is_capital_city = Column(Boolean, nullable=False, default=False)

    state = relationship('State', back_populates='cities')
    country = relationship('Country')

    def __repr__(self) -> str:
        return f"City(city_id={self.city_id!r}, name={self.name!r})"
