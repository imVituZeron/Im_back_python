entrada = input("[E]ntra [S]air: ")
senha = input("Senha: ")

senha_super_segura = "123456"

if entrada == "E" and senha == senha_super_segura:
    print("Entrando")
else:
    print("Saindo")