'''
Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
'''

from countries import countries

def count_by_letter(countries_val):
    counts = {}
    for each in countries_val:
        letter = each[0]
        counts[letter] = counts.get(letter, 0) + 1

    return counts

result = count_by_letter(countries)
print(result)    