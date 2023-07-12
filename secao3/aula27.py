number = input("Digite um numero: ")
try:
    num_float = float(number)
    print(f"O dobro de {number} é {num_float*2}")
except:
    print("Não tem como converter uma string em float")