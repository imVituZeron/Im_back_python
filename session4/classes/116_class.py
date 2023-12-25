def salutation_creator(phrase, name):
    def salu():
        return f"{phrase}, {name}!"
    return salu

saluta1 = salutation_creator("Hello", "Vitor")
saluta2 = salutation_creator("Hi", "Vitor")

print(saluta1())
print(saluta2())