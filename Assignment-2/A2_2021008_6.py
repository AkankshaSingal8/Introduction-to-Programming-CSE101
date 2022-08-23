def normal_traversal(l):
    for i in l:
        for j in i:
            print(j,end=' ')
    print()
    
def alternating_traversal(l):
    for i in range(0,len(l)):
        if i%2 == 0:
            for j in l[i]:
                print(j,end=' ')
        else:
            for j in range(len(l)-1,-1,-1):
                print(l[i][j],end=' ')
    print()


def spiral_traversal(l):
    n=len(l)
    t=[]
    q=0
    p=0
    j=0
    k=0
    for i in range(0,2*n,2):
        if i==0 or i%4==0:
            inc=True
        else:
            inc=False
        if inc:
            while j<n:
                x=q
                y=p
                while y<n-j:
                    if l[x][y] not in t:
                        t.append(l[x][y])
                    y=y+1
                y-=1
                while x<n-j:
                    if l[x][y] not in t:
                        t.append(l[x][y])
                    x+=1
                x-=1
                j+=1
                break
        else:
            while k<n:
                p=y
                q=x
                while q>0+k:
                    if l[p][q] not in t:
                        t.append(l[p][q])
                    q-=1
                while p>0+k:
                    if l[p][q] not in t:
                        t.append(l[p][q])
                    p-=1
                p+=1
                q+=1
                k+=1
                break
                
    t=[str(i) for i in t]  
    s=' '.join(t)
    print(s)              
                    
        
            
def boundary_traversal(l):
    n=len(l)
    t=[]
    for i in range(n):
        if l[0][i] not in t:
            t.append(l[0][i])
        
    for j in range(n):
        if l[j][n-1] not in t:
            t.append(l[j][n-1])

    for k in range(n-1,-1,-1):
        if l[n-1][k] not in t:
            t.append(l[n-1][k])
            
    for x in range(n-1,-1,-1):
        if l[x][0] not in t:
            t.append(l[x][0])

    t=[str(i) for i in t]  
    s=' '.join(t)
    print(s)
        


def diagonal_traversal_rtol(l):
    n=len(l)
    t=[]
    for i in range(n):
        b=i
        for a in range(i+1):
            while b>=0:
                t.append(l[a][b])
                b-=1
                break
            
    for x in range(n):
        y=n-1 
        for j in range(x,n):
            while y>=x:
                if l[j][y] not in t:
                    t.append(l[j][y])
                y-=1
                break
    t=[str(i) for i in t]  
    s=' '.join(t)
    print(s)

def diagonal_traversal_ltor(l):
    n=len(l)
    t=[]
    b=n-1
    num=0
    for i in range(n):
        c=b-num
        for a in range(i+1):
            while c<=b:
                t.append(l[a][c])
                c+=1
                break
        num+=1
            
            
    for x in range(n):
        y=n-1
        z=0
        for j in range(x,n):
            while z<=y:
                if l[j][z] not in t:
                    t.append(l[j][z])
                z+=1
                break
        y-=1
            
    t=[str(i) for i in t]  
    s=' '.join(t)
    print(s)
    


ch=0
while ch<7:
    print("1. Normal Traversal")
    print("2. Alternating traversal")
    print("3. Spiral Traversal")
    print("4. Boundary traversal ")
    print("5. Diagonal traversal from right to left")
    print("6. Diagonal traversal from left to right")
    print("7. Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        n=int(input("Enter N: "))
        l=[]
        for i in range(n):
            s=input()
            t=[int(a) for a in s.split()]
            l.append(t)
        normal_traversal(l)
    elif ch==2:
        n=int(input("Enter N: "))
        l=[]
        for i in range(n):
            s=input()
            t=[int(a) for a in s.split()]
            l.append(t)
        alternating_traversal(l)
    elif ch==3:
        n=int(input("Enter N: "))
        l=[]
        for i in range(n):
            s=input()
            t=[int(a) for a in s.split()]
            l.append(t)
        spiral_traversal(l)
    elif ch==4:
        n=int(input("Enter N: "))
        l=[]
        for i in range(n):
            s=input()
            t=[int(a) for a in s.split()]
            l.append(t)
        boundary_traversal(l)
    elif ch==5:
        n=int(input("Enter N: "))
        l=[]
        for i in range(n):
            s=input()
            t=[int(a) for a in s.split()]
            l.append(t)
        diagonal_traversal_rtol(l)
    elif ch==6:
        n=int(input("Enter N: "))
        l=[]
        for i in range(n):
            s=input()
            t=[int(a) for a in s.split()]
            l.append(t)
        diagonal_traversal_ltor(l)
