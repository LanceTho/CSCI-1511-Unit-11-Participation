"""
Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile.
"""

def city_country(city_name: str, country_name: str, population: int = 1) -> str:
    return f"{city_name.title()}, {country_name.title()} - population {population}"