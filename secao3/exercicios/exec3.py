def show_list(buy_list):
    for k ,v in enumerate(buy_list):
        print(k ,v)

def insert_item_in_list(buy_list):
    value = input("Valor: ")
    buy_list.append(value)

def delete_item_in_list(buy_list, index_value):
    if index_value.isnumeric():
        for k, v in enumerate(buy_list):
            if index_value == k:
                print("AQUI TA COM O ERROOOOOOOO!!!""")
                del buy_list[index_value]
            else:
                print("Não existe esse indice!")

BUY_LIST = []

while True:
    print("Selecione uma opção")
    option = input("[i]nserir [a]pagar [l]istar: ").lower()

    if option != "i" and option != "a" and option != "l":
        print("opção invalida!")
        continue

    if option == "i":
        insert_item_in_list(BUY_LIST)
    elif option == "a":
        index = input("Digite o indice que quer apagar: ")
        delete_item_in_list(BUY_LIST, index)
    elif option == "l":
        show_list(BUY_LIST)


