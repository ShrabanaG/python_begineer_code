'''
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Use map to create a new list by changing each country to uppercase in the countries list
Use map to create a new list by changing each number to its square in the numbers list
Use map to change each name to uppercase in the names list
'''

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(num):
    return num ** 2

def name_uppercase(country):
    return country.upper()

countries_upper_case = map(name_uppercase, countries);
square_numbers = map(square, numbers);
print(list(square_numbers))
print(list(countries_upper_case))