lista_a = ['Vitor', 'Jorge']
# o metodoos .copy() serve para copiar um lista, pois se voce so colocar o sinal de = vai esta direcionando para a mesmo lugar de memoria
lista_b = lista_a.copy() 
lista_a[0] = 'Qualquer coisa' 
print(lista_a)
print(lista_b)
