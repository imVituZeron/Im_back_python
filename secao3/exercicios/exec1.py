primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor.isnumeric() and segundo_valor.isnumeric():
    int(primeiro_valor)
    int(segundo_valor)
    if primeiro_valor > segundo_valor:
        print(f"{primeiro_valor=} é maior que {segundo_valor=}")
    elif primeiro_valor < segundo_valor:
        print(f"{segundo_valor=} é maior que {primeiro_valor=}")
    else:
        print(f"{primeiro_valor=} é igual ao {segundo_valor=}")
else:
    print("Valores não são numericos!")
