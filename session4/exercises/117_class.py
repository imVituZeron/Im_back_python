def multiply_creator(mul=int):
    def multiply(num=int):
        return num * mul
    return multiply

d = multiply_creator(2)
t = multiply_creator(3)
q = multiply_creator(4)

print(d(2))
print(t(2))
print(q(2))
