contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue
    if contador >= 10 and contador <= 27:
        print("nao vou mostra o", contador)
        continue
    
    if contador == 40:
        break
    print(contador)
print("Acabou")