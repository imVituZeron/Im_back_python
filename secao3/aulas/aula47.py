import os
secret = "amor"
correct_letter = ""

count = 0
while True:
    letter = input("Digite uma letra: ").lower()
    count += 1
    if len(letter) > 1:
        print("Digite apenas uma letra!")
        continue
            
    if letter in secret:
        correct_letter += letter

    format_word = ""
    for secret_letter in secret:
        if secret_letter in correct_letter:
            format_word += secret_letter
        else:
            format_word += "*"
    
    print(f"Palavra formatada: {format_word}")
    if format_word == secret:
        os.system("clear")
        print("Acertou todas as letras da palavra certa!")
        print(f"A palavra correta é {secret}")
        print(f"Foram {count} tentativas")
        correct_letter = ""
        count = 0
