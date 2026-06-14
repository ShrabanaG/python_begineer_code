'''
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world
'''

from countries_data import countries_data
from collections import Counter

for country in countries_data:
    if "languages" in country:
        print(f"{country['name']} has {len(country['languages'])} no. of languages")

lang_counter = Counter()

for country in countries_data:
    for lang in country['languages']:
        lang_counter[lang] += 1

for lang,count in lang_counter.most_common(10) :
    print(lang, count)
