def execute(function, *args):
    return function(*args)

print(
    execute(
        lambda x, y: x + y,
        2,3
    )
)

duplicate = execute(
    lambda mu: lambda nu: nu*mu,
    2
)
print(duplicate(2))

print(
    execute(
        lambda *args: sum(args),
        1,2,3,4,5,6,7,8,10
    )
)