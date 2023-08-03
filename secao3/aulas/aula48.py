string = "ABCDE" 

lista = [123, 'Vitor', True, 1.2, []]
# print(type(lista))

print(f"Valores originais {lista}")
print(lista[1])
print(lista[2], type(lista[2]))
print(lista[1], type(lista[1]))
lista[1] = "Sara"
lista[2] = False # trocando os valores da lista
print(f"Valores foram trocados {lista}")
print(lista[1], type(lista[1]))
print(lista[2], type(lista[2]))

