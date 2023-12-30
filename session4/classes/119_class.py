#person = dict(name="Vitor", lastname="De Paula")

person = {
    'name': 'Vitor',
    'lastname': 'Santos',
    'age': 23,
    'height': 1.77,
    'address': [
        {'street': 'tall', 'number': 8},
        {'street': 'tall 2', 'number': 88},
    ],
}

#print(person, type(person))
print(person['addrees']['street'])