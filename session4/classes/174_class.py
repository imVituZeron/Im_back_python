from itertools import combinations, permutations, product

def print_iter(iter):
    print(*list(iter), sep="\n")
    print()

people = ['Joao', 'Joana', 'Luiz', 'Leticia']

t_shirt = [
        ['preta', 'branca'], ['p', 'm', 'g'],
        ['male', 'fame'], ['algodao','poliester']
]


print_iter(combinations(people, 2))
print_iter(permutations(people, 2))
print_iter(product(*t_shirt))
