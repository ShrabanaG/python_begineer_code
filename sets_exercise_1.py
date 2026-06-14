'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
Exercises: Level 1
1.Find the length of the set it_companies
2.Add 'Twitter' to it_companies
3.Insert multiple IT companies at once to the set it_companies
4.Remove one of the companies from the set it_companies
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(f"Length: {len(it_companies)}")

it_companies.add('Twitter');
print(f'after adding one company:  {it_companies}')

it_companies.update(['RazorPay','PhonePay','Infosys','Accenture'])
print(f'after adding multiple company:  {it_companies}')
it_companies.remove('Amazon')
print(f'after deleting Amazon:  {it_companies}')
