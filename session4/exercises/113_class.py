def mult(*args) -> int:
    total = 1
    for n in args:
        total *= n
    
    return total

def odd_or_even(num=int):
    print("Odd") if num % 2 == 0 else print("Even")


print(mult(23,122))
odd_or_even(6001)