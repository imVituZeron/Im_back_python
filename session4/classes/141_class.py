product = {
    'name': "Caneta Azul",
    'price': 2.5,
    'category': "Office",
}

#dict comprehension
p = {
    key : value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
}
print(p)

#set comprehension
s = {value * 3 for value in range(5)}
print(s)