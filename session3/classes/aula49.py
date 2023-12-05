lista = [1,2,3,4]
lista[2] = 300
print(lista)
# deletando algum valor de uma lista pelo indece
del lista[2] 
print(lista)
# add um valor na lista
lista.append(50)
lista.append(44)
# removendo o ultimo item da lista
removido = lista.pop()
lista.append(70)
print(lista)
print(lista, "removido", removido)
