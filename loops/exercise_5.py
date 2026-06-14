#  Loop through the countries and extract all the countries containing the word land.

from countries import countries

for country in countries:
    if 'land' in country.lower():
        print(country)