a, b = 1, 2
a, b = b, a
print(a, b)

person = {
    'name': "Vitor",
    'lastname': "Santos"
}

person_data = {
    'idade': 23,
    'heigth': 1.77,
}

complete_person = {**person, **person_data}


def show_arguments(*args, **kwargs):
    print("Unamed", args)

    for k, v in kwargs.items():
        print(k, v)

show_arguments("colorado",nome="JOO", qlq=123)
