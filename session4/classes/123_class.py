p1 = {
    'name': "Vitor",
    'lastname': "Santos",
}


print(p1.get("name"))

#Pop method catch one especify key and
#delete the key of dict
#name = p1.pop("name")
#print(name)
#print(p1)


#Popitem method catch last key and
#delete the key of dict
lastname = p1.popitem()
print("lastname -> ", lastname)
print("p1 -> ", p1)

p1.update({
    'name' : "Sara",
    'age' : 22,
}) # or p1.update(name="Sara",age=22)

print("p1 alfter update -> ", p1)