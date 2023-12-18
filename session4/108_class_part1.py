x = 1

def scope():
    global x # manipulating x of out
    y = "lambda"
    x = 10

    # function in function
    def outher_scope():
        global x
        x = "LALALA"
        print(x)
    outher_scope()
    
    # lambda function
    anouther_scope = lambda: print(y)
    anouther_scope()

    print(x)

scope()
