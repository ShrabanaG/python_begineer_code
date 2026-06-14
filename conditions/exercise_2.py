'''
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
     * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'AI'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person['skills'] :
    left = 0
    right = len(person['skills']) - 1
    mid = int((left+right)/2)
    if len(person['skills']) % 2 == 0 :
        
        print(f'Middle skill: {person['skills'][mid]} {person['skills'][mid + 1]}') 
    else :
        print(f"Middle skill: {person['skills'][mid]}")
else :
    print('Skills are not exists')
