l1 = [
    {'name': 'Vitor', 'lastname': 'Santos'},
    {'name': 'Leandro', 'lastname': 'Santos'},
    {'name': 'Eliza', 'lastname': 'De Paula'},
    {'name': 'Ana Elisa', 'lastname': 'De Paula'},
    {'name': 'Sara', 'lastname': 'Stefani'},
]

peer_name = sorted(l1, key=lambda item: item['name'])
peer_lastname = sorted(l1, key=lambda item: item['lastname'])

for item in peer_name: print('Already order peer name: ', item)
for item in peer_lastname: print('Already order peer lastname: ', item)