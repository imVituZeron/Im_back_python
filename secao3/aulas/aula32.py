# num = input("Digite um numero inteiro: ")
# if num.isdigit():
#     if int(num) % 2 == 0:
#         print(f"O numero digita é par")
#     else:
#         print(f"O numero digita é impar")
# else:
#     print(f"O numero digitado nao é um numero inteiro!")

# -----------------------------------
hora = input("Que horas são: ")

try:
    entrada = int(hora)
    if entrada >= 0 and entrada <= 11:
        print("Bom dia")
    elif entrada >= 12 and entrada <= 17:
        print("Bom Tarde")
    elif entrada >=18 and entrada <= 23:
        print("Boa noite")
    else:
        print("Nao conheço essa hora")
except:
    print("Por favor, digite um numero!")

# ------------------------------------
nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande!")