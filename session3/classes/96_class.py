string = 'ABCD'
lista = ['Sara', 'Jorge',1,2,3, 'Ernesto']
tupla = 'Python', 'is', 'cool!'

classrooms = [
    ["maria", "helena"],
    ["Vitor"],
    ["Sara", "Eliza", "Leandro", (0,10,20,30,40)]
]

print(*lista) # iterating with print
print(*string)
print(*tupla)

print(*classrooms, sep='\n')