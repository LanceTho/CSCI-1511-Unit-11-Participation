"""
Write a function called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string
"""
import pytest
from functions.city_functions import city_country

def test_city_country() -> None:
    assert city_country("santiago", "chile") == "Santiago, Chile - population 1"

def test_city_country_population() -> None:
    assert city_country("santiago", "chile", 5000000) == "Santiago, Chile - population 5000000"