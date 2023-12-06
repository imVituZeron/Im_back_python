string_cpf = "995.724.250"
string_without_dot = string_cpf.split('.')
join_strings = ''.join(string_without_dot) 

total_sum = 0
count = 10
for num in join_strings:
    total_sum += int(num) * count
    print(f"{num} X {count} = {total_sum}")
    count -= 1

result = (total_sum * 10) % 11
if result > 9:
    first_number = 0
else:
    first_number = result

print(first_number)

