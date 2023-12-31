#useful methods

person = {
    'name' : "Vitor",
    'lastname' : "Santos",
}

print(len(person))
print(person.keys())
print(person.values())
print(person.items())
# setting with default one key
print(person.setdefault('lastlast', 0))