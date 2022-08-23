class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def object_info(self):
        data = self.fname+' '+self.lname+' '+str(self.age)
        return(data)


def sort_attribute(l,q):
    person=[]
    fname=[]
    lname=[]
    age=[]
    for i in l:
        d = i.object_info()
        t=d.split()
        person.append(t)
        fname.append(t[0])
        lname.append(t[1])
        age.append(int(t[2]))
        
    if q == "firstname":
        fname.sort()
        for fnm in fname:
            for i in range(0, len(person)):
                if person[i][0]==fnm:
                    s=' '.join(person[i])
                    print(s)
            
    elif q == "lastname":
        lname.sort()
        for lnm in lname:
            for i in range(0, len(person)):
                if person[i][1]==lnm:
                    s=' '.join(person[i])
                    print(s)
                    
    elif q == "age":
        age.sort()
        for a in age:
            for i in range(0, len(person)):
                if person[i][2]==age:
                    s=' '.join(person[i])
                    print(s)
        
print("Welcome to the Application!")
n = int(input("Specify number of people to be enrolled: "))
l=[]
for i in range(n):
    fnm = input("Enter Firstname: ")
    lnm = input("Enter Lastname: ")
    age = int(input("Enter age: "))
    p = Person(fnm, lnm, age)
    l.append(p)
q='firstname'
sort_attribute(l,q)

k = int(input("Specify number of Queries: "))
for j in range(k):
    q = input("Enter Query: ")
    sort_attribute(l,q)

