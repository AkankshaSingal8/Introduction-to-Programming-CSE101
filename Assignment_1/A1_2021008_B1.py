def combopack1(item1,item2,d1):
    tot=item1+item2
    dis= (d1*tot)/100
    price=tot-dis
    return(price)
    
def combopack2(item1,item3,d2):
    tot=item1+item3
    dis= (d2*tot)/100
    price=tot-dis
    return(price)
    
def combopack3(item3,item2,d3):
    tot=item3+item2
    dis= (d3*tot)/100
    price=tot-dis
    return(price)
    
def supersaver(item1,item2,item3):
    d=28
    tot=item3+item2+item1
    dis=(d*tot)/100
    price=tot-dis
    return(price)    
    
item1=float(input("Enter price of Item1: "))
item2=float(input("Enter price of Item2: "))
item3=float(input("Enter price of Item3: "))
print("-------------------------")
print("Discount details")
d1=float(input("Enter discount(in percentage) for 1st saver combo: "))
d2=float(input("Enter discount(in percentage) for 2nd saver combo: "))
d3=float(input("Enter discount(in percentage) for 3rd saver combo: "))
print("-------------------------")
while True:
    ph=int(input("Provide 10 digit phone number: "))
    if len(str(ph))==10:
        break
print("The resulting catalouge is")
print("-------------------------")
print("Delhi Days \nR-Block, Model Town 3 \nDelhi:110009")
print("-------------------------")
print("Item  \t\t Price(per pack)")
print("Item1 \t\t ",item1)
print("Item2 \t\t ",item2)
print("Item3 \t\t ",item3)
print("ComboPack1 \t ",combopack1(item1,item2,d1))
print("ComboPack2 \t ",combopack2(item1,item3,d2))
print("ComboPack3 \t ",combopack3(item3,item2,d3))
print("SuperSaver \t ",supersaver(item1,item2,item3))
print("-------------------------")
print("For home delivery, Contact here: ",ph)

