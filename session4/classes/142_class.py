l = ['a', 1, 1.1, True, [0,1,2], (1,2), {0,1}, {'name': "Vitor"}]

for i in l:
    if isinstance(i, set):
        print("SET")
        print(i, isinstance(i, set))

    elif isinstance(i, str):
        print("STR")
        print(i, isinstance(i, set))

    elif isinstance(i, (int, float)):
        print("INT OR FLOAT ")
        print(i, i * 2)

    else:
        print("OUTRO")
        print(i)