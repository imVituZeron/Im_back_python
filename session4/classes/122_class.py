person = {
    'name':"Vitor",
    'lastname': "Santos",
}

# No copy, this line does that person1 variable is
# pointing the same memory location which person variable.
person1 = person

# this line yes, make the shallow copy of person variable
person2 = person.copy()

person1['name'] = 10000
print(person)
person2['lastname'] = 2222
print(person)
print(person2)

