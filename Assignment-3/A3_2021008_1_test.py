import math

def matmul(a,b):
    ra = len(a)
    ca = len(a[0])
    rb = len(b)
    cb = len(b[0])
    mat=[[0 for i in range(cb)] for j in range (ra)]
    for i in range(ra):
        for j in range(cb):
            mat[i][j]=0
            for k in range(ca):
                mat[i][j]+= a[i][k]*b[k][j]
    return(mat)


def scaling(sx,sy,sz,x,y,z):
    xdash = [sx*i for i in x]
    ydash = [sy*i for i in y]
    zdash = [sz*i for i in z]
    return(xdash,ydash,zdash)

def translating(tx,ty,tz,x,y,z):
    xdash=[tx+i for i in x]
    ydash=[ty+i for i in y]
    zdash=[tz+i for i in z]
    return(xdash,ydash,zdash)

def rotation_x(angle,x,y,z):
    cos=math.cos(angle)
    sin=math.sin(angle)
    x_dash=x
    y_dash=[y[i]*cos-z[i]*sin for i in range(len(y))]
    z_dash=[y[i]*sin+z[i]*cos for i in range(len(y))]
    return(x_dash,y_dash,z_dash)
    
def rotation_y(angle,x,y,z):
    cos=math.cos(angle)
    sin=math.sin(angle)
    x_dash=[x[i]*cos+z[i]*sin for i in range(len(x))]
    y_dash=y
    z_dash=[-x[i]*sin+z[i]*cos for i in range(len(x))]
    return(x_dash,y_dash,z_dash)

def rotation_z(angle,x,y,z):
    cos=math.cos(angle)
    sin=math.sin(angle)
    x_dash=[x[i]*cos-y[i]*sin for i in range(len(x))]
    y_dash=[x[i]*sin+y[i]*cos for i in range(len(x))]
    z_dash=z
    return(x_dash,y_dash,z_dash)

def test_matmul(A, B, true_c):
    try:
        res = matmul(a,b)
        assert res == true_c
        return("True")
    except AssertionError:
        return("False")
        

def test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    try:
        x_dash,y_dash,z_dash = scaling(sx,sy,sz,x,y,z)
        assert x_dash == true_x and y_dash == true_y and z_dash == true_z
        return("True")
    except AssertionError:
        return("False")

def test_rotate(x, y, z, axis, angle, true_x, true_y, true_z):
    try:
        if axis =='x':
            x_dash,y_dash,z_dash = rotation_x(angle,x,y,z)
        elif axis =='y':
            x_dash,y_dash,z_dash = rotation_y(angle,x,y,z)
        elif axis =='z':
            x_dash,y_dash,z_dash = rotation_z(angle,x,y,z)
        assert x_dash == true_x and y_dash == true_y and z_dash == true_z
        return("True")
    except AssertionError:
        return("False")

def test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    try:
        x_dash,y_dash,z_dash = translating(tx,ty,tz,x,y,z)
        assert x_dash == true_x and y_dash == true_y and z_dash == true_z
        return("True")
    except AssertionError:
        return("False")

ch=0
while ch<5:
    print("1. Matrix Multiplication")
    print("2. Scaling")
    print("3. Translating")
    print("4. Rotation")
    ch=int(input("Enter choice: "))
    if ch == 1:
        a=[]
        ra=int(input("Enter number of rows for A: "))
        ca=int(input("Enter number of columns for A: "))
        for i in range(ra):
            c = input("Enter space separated column for A: ")
            l = [float(i) for i in c.split()]
            a.append(l)
        b=[]
        for j in range(ca):
            cb = input("Enter space separated column for B: ")
            t = [float(i) for i in cb.split()]
            b.append(t)
            
        true_c=[]
        n = int(input("Enter number of rows for resultant matrix:"))
        for i in range(n):
            v=input("Enter space separated column")
            x=[float(i) for i in v.split()]
            true_c.append(x)        
        print(test_matmul(a,b,true_c))

    elif ch == 2:
        n=int(input("Enter number of vertices for the 3D shape: "))
        s1=input("X: ")
        x=[float(i) for i in s1.split()]
        s2=input("Y: ")
        y=[float(i) for i in s2.split()]
        s3=input("Z: ")
        z=[float(i) for i in s3.split()]
        sx=float(input("Enter sx:"))
        sy=float(input("Enter sy:"))
        sz=float(input("Enter sz:"))
        s4=input("X': ")
        true_x=[float(i) for i in s4.split()]
        s5=input("Y': ")
        true_y=[float(i) for i in s5.split()]
        s6=input("Z': ")
        true_z=[float(i) for i in s6.split()]
        print(test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z))

    elif ch == 3:
        n=int(input("Enter number of vertices for the 3D shape: "))
        s1=input("X: ")
        x=[float(i) for i in s1.split()]
        s2=input("Y: ")
        y=[float(i) for i in s2.split()]
        s3=input("Z: ")
        z=[float(i) for i in s3.split()]
        tx=float(input("Enter sx:"))
        ty=float(input("Enter sy:"))
        tz=float(input("Enter sz:"))
        s4=input("X': ")
        true_x=[float(i) for i in s4.split()]
        s5=input("Y': ")
        true_y=[float(i) for i in s5.split()]
        s6=input("Z': ")
        true_z=[float(i) for i in s6.split()]
        print(test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z))

    elif ch == 4:
        n=int(input("Enter number of vertices for the 3D shape: "))
        s1=input("X: ")
        x=[float(i) for i in s1.split()]
        s2=input("Y: ")
        y=[float(i) for i in s2.split()]
        s3=input("Z: ")
        z=[float(i) for i in s3.split()]
        angle=float(input("Enter angle: "))
        axis = input("Enter axis: ")
        
        s4=input("X': ")
        true_x=[float(i) for i in s4.split()]
        s5=input("Y': ")
        true_y=[float(i) for i in s5.split()]
        s6=input("Z': ")
        true_z=[float(i) for i in s6.split()]
        print(test_rotate(x, y, z, axis, angle, true_x, true_y, true_z))



    

