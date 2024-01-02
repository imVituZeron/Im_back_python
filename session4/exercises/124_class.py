questions = [
    {
        'Question': 'Quanto é 2+2?',
        'Options' : ['1', '3', '4', '5'],
        'response': '4',
    },
    {
        'Question': 'Quanto é 5*5?',
        'Options' : ['25', '55', '10', '51'],
        'response': '25',
    },
    {
        'Question': 'Quanto é 10/2?',
        'Options' : ['4', '5', '2', '1'],
        'response': '5',
    },
]

checks = 0
for question in questions:
    print(f"Pergunta: {question['Question']}")
    print()

    for k, i in enumerate(question['Options']):
        print(f"{k}) {i}")

    print()
    choose = input("Escolha uma opção: ")

    if choose.isdigit():
        if question['response'] == question['Options'][int(choose)]:
            checks += 1
            print("Acertou :))")
            print()
    else:
        print("Errouu :((")
        print()

print(f"Você acertou {checks}, de {len(questions)} perguntas")
print()