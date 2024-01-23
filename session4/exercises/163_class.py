def summ(x, y):
    return x + y

def mult(x, y):
    return x * y

def create_function(function, x):
    def internal(y):
        return function(x, y)
    return internal


summm = create_function(summ, 1)
multii = create_function(mult, 13)
print(summm(4))
print(multii(4))

