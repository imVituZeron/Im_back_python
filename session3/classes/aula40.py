""" Calculadora com while """
def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

while True:
    num1 = input("Digite um numero: ")
    num2 = input("Digite um numero: ")
    operador = input("Digite um operador [+-*/]: ")
    
    if num1.isdigit() and num2.isdigit():
        if operador == "+":
            print(soma(float(num1),float(num2)))
        elif operador == "-":
            print(sub(float(num1),float(num2)))
        elif operador == "*":
            print(mult(float(num1),float(num2)))
        elif operador == "/":
            print(div(float(num1),float(num2)))
        else:
            print("Operador invalido")
            continue
    else:
        print("Um ou ambos numeros invalidos")
        continue

    sair = input("Deseja sair? [s]im: ").lower()
    if sair == "s":
        break

