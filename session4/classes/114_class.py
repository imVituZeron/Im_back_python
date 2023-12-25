def message(msg, name=str) -> str:
    return f"{msg}, {name}"

def execute(function, *args):
    return function(*args)


print(
    execute(message, "Hello", "Vitor"),
    execute(message, "Good morning", "Vitor"),
    execute(message, "Good night", "Vitor")
)