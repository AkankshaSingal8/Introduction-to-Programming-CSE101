global cid
cid = 1
class LaundryService:
    def __init__(self,name,no,email,ctype,brand,season):
        self.name = name
        self.num = no
        self.email = email
        self.type = ctype
        self.brand = brand
        self.season = season
        self.id=cid
    def customerDetails(self):
        data="\nThe customer specific details are:\n\n"
        data+="Customer Id: "+str(self.id)+'\n'
        data+="Customer Name: "+self.name+'\n'
        data+="Contact: "+str(self.num)+'\n'
        data+="Email: "+self.email+'\n'
        data+="Type of Cloth: "+self.type+'\n'
        data+="Branded: "+str(self.brand)+'\n'
        data+="Season: "+self.season+'\n'
        return(data)
    
    def calculateCharge(self):
        if self.type == 'Cotton':
            charge = 50
        elif self.type == 'Silk':
            charge = 30
        elif self.type == 'Woolen':
            charge = 90
        elif self.type == 'Polyester':
            charge = 20
        if self.brand:
            charge *= 1.5
        if self.season == 'Winter':
            charge /= 2
        else:
            charge *= 2
            
        return(charge)
    
    def finalDetails(self):
        print(LaundryService.customerDetails(self))
        ch = LaundryService.calculateCharge(self)
        if ch > 200:
            return("Total charge: "+str(ch)+"\nTo be returned in 4 days\n")
        else:
            return("Total charge: "+str(ch)+"\nTo be returned in 7 days\n")

n=int(input("Enter number: "))
for i in range(n):
    nm = input("Name of customer: ")
    while True:
        num = int(input("Contact Number: "))
        if len(str(num)) == 10:
            break
    em = input("Email: ")
    ct = input("Type of cloth: ")
    b = int(input("Branded?: "))
    s = input("Season: ")
    if b:
        brand=True
    else:
        brand=False
    customer = LaundryService(nm,num,em,ct,brand,s)
    print(customer.finalDetails())
    cid+=1
