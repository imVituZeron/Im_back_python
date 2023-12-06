condition = 10 == 11
variable = "value" if condition else "another value"
print(variable)

digit = 9
ternarie = digit if digit <= 9 else 0
invert_ternarie = 0 if digit > 9 else digit
print(ternarie, invert_ternarie)

print('value' if False else 'another value' if False else "end") # confuse