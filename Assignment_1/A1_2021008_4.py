def f1():
    b1=False
    for i in range(2):
        fn= b1 and (not b1)
        if fn == True:
            print("Satisfiable")
            print(b1,not b1)
            return
        b1= True
    else:
        print("Unsatisfiable")


def f2():
    b1=False
    b2=False
    b3=False
    for i in range(2):
        fn=(b1 or b2) and (b2 or not b3)
        if fn == True:
            print("Satisfiable")
            print(b1,b2,b3)
            return
        b3=True
       
    b2=True
    b3=False
    for i in range(2):
        fn=(b1 or b2) and (b2 or not b3)
        if fn == True:
            print("Satisfiable")
            print(b1,b2,b3)
            return
        b3=True
        
    b1=True
    b2=False
    b3=False
    for i in range(2):
        fn=(b1 or b2) and (b2 or not b3)
        if fn == True:
            print(fn)
            print("Satisfiable")
            print(b1,b2,b3)
            return
        b3=True
    
    b2=True
    b3=False
    for i in range(2):
        fn=(b1 or b2) and (b2 or not b3)
        if fn == True:
            print("Satisfiable")
            print(b1,b2,b3)
            return
        b3=True
    else:
        print("Unsatisfiable")
    
f1()
f2()
