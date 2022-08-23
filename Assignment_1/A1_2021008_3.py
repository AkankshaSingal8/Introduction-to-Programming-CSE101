print("Provide polynomial function details:")
e=int(input("Enter Degree of the polynomial: "))
l=[]
for i in range(e+1):
    c=int(input("Coefficient:"))
    l.append(c)

lb=int(input("Lower bound for X:"))
ub=int(input("Upper bound for X: "))
d=int(input("Steps in which you wish to increment X: "))

print(" ------------------------------------")
if e == 0:
    for i in range(lb,ub+1,d):
        y=l[0]
        if y>=0:
            print("|",end='')
            print("*"*y)
        else:
            print(" "*abs(y),end='')
            print("|")
    
if e==1:
    for i in range(lb,ub+1,d):
        y=l[0]*i+l[1]
        if y>=0:
            print("|",end='')
            print("*"*y)
        else:
            print(" "*abs(y),end='')
            print("|")
        
if e==2:
    for i in range(lb,ub+1,d):
        y=l[0]*(i**2)+l[1]*i+l[2]
        if y>=0:
            print("|",end='')
            print("*"*y)
        else:
            print(" "*abs(y),end='')
            print("|")
        
if e==3:
    for i in range(lb,ub+1,d):
        y=l[0]*(i**3)+l[1]*(i**2)+l[2]*i+l[3]
        if y>=0:
            print("|",end='')
            print("*"*y)
        else:
            print(" "*abs(y),end='')
            print("|")

        
