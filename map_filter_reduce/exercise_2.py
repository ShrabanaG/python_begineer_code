'''
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
Use filter to filter out countries containing 'land'.
Use filter to filter out countries having exactly six characters.
Use filter to filter out countries containing six letters and more in the country list.
Use filter to filter out countries starting with an 'E'
'''

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def filter_land(country):
    if (country.startswith('E')):
        return True
    else:
        return False

countries_with_land = filter(filter_land, countries)

print(list(countries_with_land))