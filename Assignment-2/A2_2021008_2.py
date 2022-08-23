import math

def scaling(sx,sy,sz,x,y,z):
    xdash=[sx*i for i in x]
    ydash=[sy*i for i in y]
    zdash=[sz*i for i in z]
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
      
n=int(input("Enter number of vertices for the 3D shape: "))
s1=input("X: ")
x=[int(i) for i in s1.split()]
s2=input("Y: ")
y=[int(i) for i in s2.split()]
s3=input("Z: ")
z=[int(i) for i in s3.split()]

with open("transformations.txt","w") as f:
    s=s1+'\n'+s2+'\n'+s3+'\n'
    f.write(s)

q=int(input("Enter number of query: "))
for i in range(q):
    que=input("Enter query: ")
    query=[i for i in que.split()]
    if query[0]=='S':
        sx=int(query[1])
        sy=int(query[2])
        sz=int(query[3])
        x_dash,y_dash,z_dash = scaling(sx,sy,sz,x,y,z)
        x_d=' '.join(str(i) for i in x_dash)
        print("x': ",x_d)
        y_d=' '.join(str(i) for i in y_dash)
        print("y': ",y_d)
        z_d=' '.join(str(i) for i in z_dash)
        print("z': ",z_d)
            
    elif query[0]=='T':
        tx=int(query[1])
        ty=int(query[2])
        tz=int(query[3])
        x_dash,y_dash,z_dash=translating(tx,ty,tz,x,y,z)
        x_d=' '.join(str(i) for i in x_dash)
        print("x': ",x_d)
        y_d=' '.join(str(i) for i in y_dash)
        print("y': ",y_d)
        z_d=' '.join(str(i) for i in z_dash)
        print("z': ",z_d)

    elif query[0]=='R':
        axis=query[1]
        angle=float(query[2])
        if axis=='x':
            x_dash,y_dash,z_dash=rotation_x(angle,x,y,z)
            x_d=' '.join(str(i) for i in x_dash)
            print("x': ",x_d)
            y_d=' '.join(str(i) for i in y_dash)
            print("y': ",y_d)
            z_d=' '.join(str(i) for i in z_dash)
            print("z': ",z_d)
            
        elif axis=='y':
            x_dash,y_dash,z_dash=rotation_y(angle,x,y,z)
            x_d=' '.join(str(i) for i in x_dash)
            print("x': ",x_d)
            y_d=' '.join(str(i) for i in y_dash)
            print("y': ",y_d)
            z_d=' '.join(str(i) for i in z_dash)
            print("z': ",z_d)
            
        elif axis=='z':
            x_dash,y_dash,z_dash=rotation_z(angle,x,y,z)
            x_d=' '.join(str(i) for i in x_dash)
            print("x': ",x_d)
            y_d=' '.join(str(i) for i in y_dash)
            print("y': ",y_d)
            z_d=' '.join(str(i) for i in z_dash)
            print("z': ",z_d)
    
    with open("transformations.txt","a") as f:
        s=' '.join(str(i) for i in x_dash)
        s+='\n'
        s+=' '.join(str(i) for i in y_dash)
        s+='\n'
        s+=' '.join(str(i) for i in z_dash)
        s+='\n'
        f.write(s)
        
        
'''0 0 0 0 4 4 4 4
y = 0 0 3 3 3 0 0 3
z = 0 2 2 0 0 0 2 2'''
