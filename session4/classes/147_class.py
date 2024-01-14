def generator(n=0, max=10):
    while True:
        yield n
        n += 1

        if n > max:
            return 
        
gen = generator(max=8)
for n in gen:
    print(n)