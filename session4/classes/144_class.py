string = "Vitor"
method = "upper"

print(dir(string))
print(string.__sizeof__())
print(string.__len__())

# verificate method object with hasattr
if hasattr(string, method):
    print("TEM UPPER")
    #execute the method
    print(getattr(string, method)())