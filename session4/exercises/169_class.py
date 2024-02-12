from itertools import zip_longest

def zipper(l1: list[str], l2: list[str]):

    interval = min(len(l1), len(l2))

    return [(l1[i], l2[i]) for i in range(interval)]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2)) # -> my type
print(list(zip(l1, l2))) # -> built-in 
print(list(zip_longest(l1, l2))) # -> also built-in