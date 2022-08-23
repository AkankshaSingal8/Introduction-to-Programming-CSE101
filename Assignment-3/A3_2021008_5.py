class Student:
    def __init__(self,name,cgpa,branch):
        self.name = name
        self.cgpa = cgpa
        self.branch = branch
        self.isPlaced = False
        self.Eligible = False
        
    def isEligible(self,cmpny):
        rcgpa = cmpny.getrcgpa()
        branches = cmpny.getbranches()
        nm = cmpny.getname()        
        if self.cgpa>=rcgpa and (self.branch in branches) and self.isPlaced==False:
            print(f"Student {self.name} is eligible for Company {nm}")
            self.Eligible = True
        else:
            self.Eligible = False
            print(f"Student {self.name} is not eligible for Company {nm}")
        return(self.Eligible)

    def apply(self,cmpny):
        if self.Eligible:
            cmpny.appliedstudents(self)
        
    def getcgpa(self):
        return(self.cgpa)
    
    def getname(self):
        return(self.name)

    def getsPlaced(self):
        self.isPlaced = True
        return(self.isPlaced)

class Company:
    def __init__(self, name, rcgpa, branches, positionopen):
        self.name = name
        self.reqcgpa = rcgpa
        self.branches = branches
        self.open = positionopen
        self.appliedStudents = []
        self.applicationOpen = True
        
    def hireStudents(self):
        hired = []
        t=[]
        for d in self.appliedStudents:
            l=[d.getname(),d.getcgpa()]
            t.append(l)
        if t==[]:
            print("Did not Hire any candidates")
            return
        
        for i in range (self.open):
            maxgpa=-1
            for student in t:
                if student[1]>maxgpa:
                    maxgpa = student[1]
       
            for j in range (len(t)):
                if t[j][1]==maxgpa:
                    hired.append(t[j][0])
                    stud_obj=self.appliedStudents[j]
                    stud_obj.getsPlaced()
                    t.pop(j)
                    self.appliedStudents.pop(j)
                    break
        print(f"The company {self.name} has hired the following candidates:")
        for name in hired:
            print(name)
        no=len(hired)
        print(f"The company hired {no} students")
        self.closeApplication()
                
    def closeApplication(self):
        self.applicationOpen = False
        
    def getrcgpa(self):
        return(self.reqcgpa)
    
    def getname(self):
        return(self.name)
    
    def getbranches(self):
        return(self.branches)
        
    def appliedstudents(self,student):
        self.appliedStudents.append(student)

'''s=Student('bb',10,'CSE')
s2=Student('aa',5,'CSE')
s3=Student('cc',5,'CSE')
c=Company('g',7,['CSE','CSAI'],2)
if s.isEligible(c):
    s.apply(c)
if s2.isEligible(c):
    s2.apply(c)
if s3.isEligible(c):
    s3.apply(c)
c.hireStudents()
s.isEligible(c)
s2.isEligible(c)
s3.isEligible(c)'''


n = int(input("Enter number of students: "))
sdata=[]
for i in range(n):
    nm = input("Enter name of student: ")
    while True:
        try:
            cgpa = float(input("Enter cpga: "))
            assert cgpa>=0 and cgpa<=10
            break
        except AssertionError:
            print("Please provide a valid cgpa")
    branch = input("Enter branch: ")
    l=Student(nm,cgpa,branch)
    sdata.append(l)
    
 
k = int(input("Enter number of Companies: "))
for j in range(k):
    cnm = input("Enter name of Company: ")
    try:
        rcgpa = float(input("Enter cpga: "))
        assert rcgpa>=0 and rcgpa<=10
    except AssertionError:
        print("Please provide a valid cgpa")

    branch = input("Enter space separated branches of the Company: ")
    branches = [i for i in branch.split()]
    pos = int(input("Enter number of positions open for the company: "))
    comp = Company(cnm, rcgpa, branches, pos)
    for student in sdata:
        eligibility = student.isEligible(comp)
        if eligibility:
            student.apply(comp)
    comp.hireStudents()
    
