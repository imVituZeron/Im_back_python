def sun(x, y) -> int:
    if x > 10:
        return x
    return x + y

result = sun(12,2)
result1 = sun(2,4)
print(result + result1)