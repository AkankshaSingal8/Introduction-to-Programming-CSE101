c=int(input("Enter initial cost: "))
dr=int(input("Enter deprication rate: "))
m=0
dcost=(dr*c)/100
own_cost=c
val=50
for i in range(1,6):
    m+=c/100
    own_cost=own_cost-dcost-m
    val=val+(10*val)/100
    utility= 6000*val
    if own_cost<utility:
        print(i)
        break
    
for j in range(6,16):
    m+=(50*m)/100
    own_cost=own_cost-dcost-m
    val=val+(10*val)/100
    utility= 6000*val
    if own_cost<utility:
        print(j)
        break
else:
    print("After 15 years")
