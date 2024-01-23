import copy

prods = [
    {"name": "Product 5", "price": 10.00},
    {"name": "Product 1", "price": 22.32},
    {"name": "Product 3", "price": 10.11},
    {"name": "Product 2", "price": 105.87},
    {"name": "Product 4", "price": 69.90},
]

def more_ten_percent(prods: list[dict]) -> list[dict]:
    
    new_prods = [
            {**prod, "price": prod["price"] + (prod["price"] * 0.1)}
            for prod in copy.deepcopy(prods)
    ]

    return new_prods


def ordinating_by_name(prods: list[dict]) -> list[dict]:

    new_prods = sorted(prods, key=lambda p: p['name'], reverse=True)

    return new_prods


def ordinating_by_price(prods: list[dict]) -> list[dict]:

    new_prods = sorted(prods, key=lambda p: p['price'])
    
    return new_prods

print(*prods)
print(*more_ten_percent(prods), sep='\n')
print()
print(*ordinating_by_name(prods), sep='\n')
print()
print(*ordinating_by_price(prods), sep='\n')
