person = {}

key = 'name'

person[key] = "Vitor"
person['lastname'] = "Santos"

print(person[key])

person[key] = "Sara" # Overlapping the key with another value
del person["lastname"] # deleting the key

# Verify if lastname key exist or not!
if person.get('lastname') is None:
    print("Not exist!")
else:
    print(person['lastname'])