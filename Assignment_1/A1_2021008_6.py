def derivative(x,n):
    return(n*(x**(n-1)))

def find_roots(l):
    n=1        
    while True:
        d=0.0
        val=0.0
        
        for i in l:
            val += n**i
            d += derivative(n,i)
        
        if type(val)==complex:
            print("The value is Complex")
            print("The closest root is: ",int(n))
            break
                        
        elif (val<=0.001 and val>=(-0.001)):
            print("The root is: ",n)
            break
               
        n= n - (val/d)
        


n=int(input("Enter number of terms: "))
l=[]
for i in range(n):
    x=float(input("Enter exponent: "))
    l.append(x)
find_roots(l)
