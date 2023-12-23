def summ(*args) -> int:
    total = 0
    for i in args:
        total += i

    return total

print(summ(1,2,3,4,5,6,1,2,23,3,4,5,11,100))