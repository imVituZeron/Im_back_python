l = []
d = {}
c = set()
t = ()
string = ""
i = 0
f = 0.0
nothing = None
fal = False
interval = range(0)


def falsy(value):
    return "falsy" if not value else 'Trythy'

print(f'TESTE', falsy("TESTE"))
print(f'{l=}', falsy(l))
print(f'{d=}', falsy(d))
print(f'{c=}', falsy(c))
print(f'{t=}', falsy(t))
print(f'{string=}', falsy(string))
print(f'{i=}', falsy(i))
print(f'{f=}', falsy(f))
print(f'{nothing=}', falsy(nothing))
print(f'{fal=}', falsy(fal))
print(f'{interval=}', falsy(interval))
