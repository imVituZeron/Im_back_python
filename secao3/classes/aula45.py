texto = iter("Vitor")

# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

# as linhas abaixo fazem as mesmas coisas que as acima!
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

texto2 = "Jose da Silva"

iterador = iter(texto2) # passando um iter<- objeto iteravel para uma variavel

while True:
    try:
        print(next(iterador)) # passando um obejto iteravel para um funcao next onde ela itera sobre o objeto
    except StopIteration:
        break
