def decimal_to_binary(dno):
    s=''
    while dno>0:
        dig=dno%2
        dno=dno//2
        s+=str(dig)
    bno=s[::-1]
    print(bno)

def binary_to_decimal(bno):
    i=0
    dno=0
    while bno>0:
        dig=bno%10
        bno=bno//10
        dno+=dig*(2**i)
        i+=1
    print(dno)

def decimal_to_hexadecimal(dno):
    s=''
    d={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while dno>0:
        dig=dno%16
        dno=dno//16
        if dig>=0 and dig<=9:
            s+=str(dig)
        else:
            s+=d[dig]
    hno=s[::-1]
    print(hno)
    
def hexadecimal_to_decimal(hno):
    d={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    num=len(hno)-1
    dno=0
    for i in hno:
        if i.isdigit()==True:
            val=int(i)
        else:
            for dec,hexa in d.items():
                if hexa==i:
                    val=dec
        dno+=val*(16**num)
        num-=1
        
    print(dno)
    
def decimal_to_octal(dno):
    s=''
    while dno>0:
        dig=dno%8
        dno=dno//8
        s+=str(dig)
    ono=s[::-1]
    print(ono)

def octal_to_decimal(ono):
    i=0
    dno=0
    while ono>0:
        dig=ono%10
        ono=ono//10
        dno+=dig*(8**i)
        i+=1
    print(dno)


def binary_to_hexadecimal(bno):
    d={'0000':'0','0001':'1','0010':'2','0011':'3',
       '0100':'4','0101':'5','0110':'6','0111':'7',
       '1000':'8','1001':'9','1010':'A','1011':'B',
       '1100':'C','1101':'D','1110':'E','1111':'F'}
    hno=''
    if len(bno)>4:
        for i in range(-1,-len(bno)-1,-4):
            s=bno[i:i-4:-1]
            n=s[::-1]
            if len(n)<4:
                num = 4-len(n)
                n ='0'*num+n
            hno += d[n]
    else:
        num=4-len(bno)
        bno='0'*num+bno
        hno += d[bno]
    hno=hno[::-1]
    print(hno)
    
def hexadecimal_to_binary(hno):
    d={'0000':'0','0001':'1','0010':'2','0011':'3',
       '0100':'4','0101':'5','0110':'6','0111':'7',
       '1000':'8','1001':'9','1010':'A','1011':'B',
       '1100':'C','1101':'D','1110':'E','1111':'F'}
    bno=''
    for i in hno:
        for bi,hx in d.items():
            if hx==i:
                bno+=bi
    print(bno)

def binary_to_octal(bno):
    d={'000':'0','001':'1','010':'2','011':'3',
       '100':'4','101':'5','110':'6','111':'7'}
    ono=''
    if len(bno)>3:
        for i in range(-1,-len(bno)-1,-3):
            s=bno[i:i-3:-1]
            n=s[::-1]
            if len(n)<3:
                num = 3-len(n)
                n ='0'*num+n
            ono += d[n]
    else:
        num=3-len(bno)
        bno='0'*num+bno
        ono += d[bno]
    ono=ono[::-1]
    print(ono)
    

def octal_to_binary(ono):
    d={'000':'0','001':'1','010':'2','011':'3',
       '100':'4','101':'5','110':'6','111':'7'}
    bno=''
    for i in ono:
        for bi,oc in d.items():
            if oc==i:
                bno+=bi
    print(bno)
    
def hexadecimal_to_octal(hno):
    d={'0000':'0','0001':'1','0010':'2','0011':'3',
       '0100':'4','0101':'5','0110':'6','0111':'7',
       '1000':'8','1001':'9','1010':'A','1011':'B',
       '1100':'C','1101':'D','1110':'E','1111':'F'}
    bno=''
    for i in hno:
        for bi,hx in d.items():
            if hx==i:
                bno+=bi
                
    d={'000':'0','001':'1','010':'2','011':'3',
       '100':'4','101':'5','110':'6','111':'7'}
    ono=''
    if len(bno)>3:
        for i in range(-1,-len(bno)-1,-3):
            s=bno[i:i-3:-1]
            n=s[::-1]
            if len(n)<3:
                num = 3-len(n)
                n ='0'*num+n
            ono += d[n]
    else:
        num=3-len(bno)
        bno='0'*num+bno
        ono += d[bno]
    ono=ono[::-1]
    print(ono)

def octal_to_hexadecimal(ono):
    d={'000':'0','001':'1','010':'2','011':'3',
       '100':'4','101':'5','110':'6','111':'7'}
    bno=''
    for i in ono:
        for bi,oc in d.items():
            if oc==i:
                bno+=bi
                
    d={'0000':'0','0001':'1','0010':'2','0011':'3',
       '0100':'4','0101':'5','0110':'6','0111':'7',
       '1000':'8','1001':'9','1010':'A','1011':'B',
       '1100':'C','1101':'D','1110':'E','1111':'F'}
    hno=''
    if len(bno)>4:
        for i in range(-1,-len(bno)-1,-4):
            s=bno[i:i-4:-1]
            n=s[::-1]
            if len(n)<4:
                num = 4-len(n)
                n ='0'*num+n
            hno += d[n]
    else:
        num=4-len(bno)
        bno='0'*num+bno
        hno += d[bno]
    hno=hno[::-1]
    print(hno)

def radixa_to_radixb(a,b,no):
    l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
       'T','U','V','W','X','Y','Z']
    num=len(no)-1
    dno=0
    for i in no:
        if i.isdigit()==True:
            val=int(i)
        else:
            val=l.index(i)+10
            
        dno+=val*(a**num)
        num-=1

    bno=''
    while dno>0:
        dig=dno%b
        dno=dno//b
        if dig>=0 and dig<=9:
            bno+=str(dig)
        else:
            ind=dig-10
            bno+=l[ind]
    bno=bno[::-1]
    print(bno)
    

ch=0
while ch<14:
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Hexadecimal")
    print("4. Hexadecimal to Decimal")
    print("5. Decimal to Octal")
    print("6. Octal to Decimal")
    print("7. Binary to Hexadecimal")
    print("8. Hexadecimal to Binary")
    print("9. Binary to Octal")
    print("10. Octal to Binary")
    print("11. Hexadecimal to Octal")
    print("12. Octal to Hexadecimal")
    print("13. Radix A to Radix B")
    print("14. Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        while True:
            try:
                dno=int(input("Enter decimal number:"))
                break
            except(ValueError):
                print("Enter correct input")
        decimal_to_binary(dno)
        
    elif ch==2:
        while True:
            bno=input("Enter binary Number: ")
            flag=True
            for i in bno:
                if int(i)!=0 and int(i)!=1:
                    flag=False

            if flag:
                break
                    
        binary_to_decimal(int(bno))
        
    elif ch==3:
        while True:
            try:
                dno=int(input("Enter decimal number:"))
                break
            except(ValueError):
                print("Enter correct input")
        decimal_to_hexadecimal(dno)
        
    elif ch==4:
        while True:
            l=['A','B','C','D','E','F']
            hno=input("Enter hexadecimal number: ")
            flag=True
            for i in hno:
                if i.isdigit()==False and i not in l:
                    flag=False
            if flag:
                break
        hexadecimal_to_decimal(hno)
        
    elif ch==5:
        while True:
            try:
                dno=int(input("Enter decimal number:"))
                break
            except(ValueError):
                print("Enter correct input")
        decimal_to_octal(dno)
        
    elif ch==6:
        while True:
            ono=int(input("Enter octal Number: "))
            flag=True
            num=ono
            if ono<0:
                flag=False
            while num>0:
                dig=num%10
                num=num//10
                if dig>7:
                    flag=False
            if flag:
                break
        octal_to_decimal(ono)
        
    elif ch==7:
        while True:
            bno=input("Enter binary Number: ")
            flag=True
            for i in bno:
                if int(i)!=0 and int(i)!=1:
                    flag=False
                
            if flag:
                break
        binary_to_hexadecimal(bno)
        
    elif ch==8:
        while True:
            l=['A','B','C','D','E','F']
            hno=input("Enter hexadecimal number: ")
            flag=True
            for i in hno:
                if i.isdigit()==False and i not in l:
                    flag=False
            if flag:
                break
        hexadecimal_to_binary(hno)
        
    elif ch==9:
        while True:
            bno=input("Enter binary Number: ")
            flag=True
            for i in bno:
                if int(i)!=0 and int(i)!=1:
                    flag=False
                
            if flag:
                break
        binary_to_octal(bno)
        
    elif ch==10:
        while True:
            ono=int(input("Enter octal Number: "))
            flag=True
            num=ono
            if ono<0:
                flag=False
            while num>0:
                dig=num%10
                num=num//10
                if dig>7:
                    flag=False
            if flag:
                break
        octal_to_binary(str(ono))
        
    elif ch==11:
        while True:
            l=['A','B','C','D','E','F']
            hno=input("Enter hexadecimal number: ")
            flag=True
            for i in hno:
                if i.isdigit()==False and i not in l:
                    flag=False
            if flag:
                break
        hexadecimal_to_octal(hno)
        
    elif ch==12:
        while True:
            ono=int(input("Enter octal Number: "))
            flag=True
            num=ono
            if ono<0:
                flag=False
            while num>0:
                dig=num%10
                num=num//10
                if dig>7:
                    flag=False
            if flag:
                break
            
        octal_to_hexadecimal(str(ono))
        
    elif ch==13:
        a=int(input("Enter radix A: "))
        b=int(input("Enter radix B: "))
        no=input("Enter number: ")
        radixa_to_radixb(a,b,no)
        
    
