import decimal

num_1 = decimal.Decimal(0.1)
num_2 = decimal.Decimal(0.7)
numbers = num_1 + num_2

print(numbers)
print(f"{numbers:.2f}")

print(round(numbers, 2))