x = 1

def scope():
    #global x # manipulating x of out
    y = "lambda"
    x = 10

    # function in function
    def other_scope():
        #global x
        x = "LALALA"
        print(x)
    other_scope()
    
    # lambda function
    another_scope = lambda: print(y)
    another_scope()

    print(x)

scope()