import sys

l = [n for n in range(100000)] # List already save at memory
generator = (n for n in range(100000)) # The generator not, this will save one by one

print(sys.getsizeof(l))
print(sys.getsizeof(generator))

for i in generator:
    print(i)

print(next(generator))
print(next(generator))
print(next(generator))

