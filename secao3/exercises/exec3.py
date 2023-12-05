import os
def show_list(buy_list):
    os.system('clear')
    print("/-- Shop list --/")
    for k ,v in enumerate(buy_list):
        print(k ,v)
    print("/--------------/")

def insert_item_in_list(buy_list):
    os.system('clear')
    value = input("Valor: ")
    buy_list.append(value)

def delete_item_in_list(buy_list=list):
    os.system('clear')

    index = input("Digite o indice que quer apagar: ")

    if index.isnumeric():
        index = int(index)
        for k, _ in enumerate(buy_list):
            if index == k:
                print('Apagado com sucesso!')
                del buy_list[index]

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
        delete_item_in_list(BUY_LIST)
    elif option == "l":
        show_list(BUY_LIST)


