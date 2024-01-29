def function_create(func):
    def internal(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return func(*args, **kwargs)
    return internal

def invert_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("lalallla")


invert_string_check_params = function_create(invert_string)
invert = invert_string("Vitor")
print(invert)
