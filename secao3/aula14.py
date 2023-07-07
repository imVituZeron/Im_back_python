a = "A"
b = "B"
c = 1.1

# pelo parametros dos argumentos!
formato = "a={va}, b={v}, c={ve}, c={ve}".format(va=a, v=b, ve=c)


# pelo index dos argumentos
formato1 = "a={0}, b={1}, c={2}".format(a, b, c)

# pela ordem dos argumentos
formato2 = "a={}, b={}, c={}".format(a, b, c)
print(formato)
print(formato1)
print(formato2)
