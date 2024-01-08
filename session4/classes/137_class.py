product = [
    {'name': "p1", "price": 20},
    {'name': "p2", "price": 10},
    {'name': "p3", "price": 30},
]

price = [
    {**p, 'price': p['price'] * 1.05 }
    if p['price'] > 20 else {**p} 
    for p in product
]

name = [price['price'] for price in product]

print(price), print(name)
