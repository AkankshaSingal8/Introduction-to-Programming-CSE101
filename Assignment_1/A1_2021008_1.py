def right_angled_triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end='')
        print()
        
def isosceles_triangle(n):
    i=0
    x=1
    for i in range(n-1,-1,-1):
        print(" "*i,end='')
        while i<n:
            for j in range(1,x+1):
                print(j,end='')
            print()
            x+=2
            i+=1
            break
def kite(n):
    y=0
    x=1
    z=1
    for i in range(n-1,-1,-1):
        print(" "*i,end='')
        while y<n:
            for j in range(1,x+1):
                print(j,end='')
            print()
            x+=2
            y+=1
            break
    x-=4
    for i in range(1,n):
        print(" "*i,end='')
        while z<n:
            for j in range(1,x+1):
                print(j,end='')
            print()
            x-=2
            z+=1
            break
        
            
def half_kite(n):
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end='')
        print()
    for i in range(1,n):
        while(n>0):
            for j in range(1,n):
                print(j, end='')
            n-=1
            break
        print()

def x(n):
    y=0
    x=1
    z=1
    for i in range(n-1,-1,-1):
        while y<n:
            for j in range(1,x+1):
                pass
            x+=2
            y+=1
    x-=2
    for i in range(0,n-1):
        print(" "*i,end='')
        while z<n:
            for j in range(1,x+1):
                print(j,end='')
            print()
            x-=2
            z+=1
            break
    a=0
    b=1
    for i in range(n-1,-1,-1):
        print(" "*i,end='')
        while a<n:
            for j in range(1,b+1):
                print(j,end='')
            print()
            b+=2
            a+=1
            break
    
ch=0
while ch<6:
    print("------------------MENU----------------")
    print("1. Right Angled Triangle")
    print("2. Isosceles triangle")
    print("3. Kite")
    print("4. Half Kite")
    print("5. X")
    print("6. Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        n=int(input("Enter Number:"))
        right_angled_triangle(n)
    elif ch==2:
        n=int(input("Enter Number:"))
        isosceles_triangle(n)
    elif ch==3:
        n=int(input("Enter Number:"))
        kite(n)
    elif ch==4:
        n=int(input("Enter Number:"))
        half_kite(n)
    elif ch==5:
        n=int(input("Enter Number:"))
        x(n)
