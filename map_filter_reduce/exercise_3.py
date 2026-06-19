'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
Use reduce to sum all the numbers in the numbers list.
Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
'''
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

sum = reduce(lambda acc, n: acc + n, numbers)
countries_slice = reduce(lambda acc, c: acc +","+c, countries[:-1])

print(sum)
print(f"{countries_slice} and {countries[-1]} are north European countries")


