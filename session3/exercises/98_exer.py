def second_digit(ten_digits=str, first_digit=int):
    nine_plus_first = ten_digits + str(first_digit)
    
    second_total_sum = 0
    second_count = 11

    for num in nine_plus_first:
        second_total_sum += int(num) * second_count
        print(f"{num} X {second_count} = {second_total_sum}")
        second_count -= 1

    second_number = (second_total_sum * 10) % 11
    second_number = second_number if second_number <= 9 else 0
    print(second_number)
    print("---")

    return second_number


def first_digit(nine_digits=str):
    first_total_sum = 0
    first_count = 10

    for num in nine_digits:
        first_total_sum += int(num) * first_count
        print(f"{num} X {first_count} = {first_total_sum}")
        first_count -= 1

    first_number = (first_total_sum * 10) % 11
    first_number = first_number if first_number <= 9 else 0
    print(first_number)
    print("---")

    return first_number


user_cpf = "74682489070"
first_nine_digits = user_cpf[:9]

first_number = first_digit(first_nine_digits)
second_number = second_digit(first_nine_digits, first_number)

calculate_cpf = f"{first_nine_digits}{first_number}{second_number}"

print(f"CPF was given by user: {user_cpf}")
print(f"CPF was made by machine: {calculate_cpf}")

print("valid!") if user_cpf == calculate_cpf else print("invalid!")
