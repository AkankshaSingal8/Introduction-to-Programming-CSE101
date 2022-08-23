students={}
with open("Q4/Admin/RegisteredStudents.txt","r") as f:
    for i in f.readlines():
        l=i.split()
        students[l[0]]=int(l[1])


ans_key={}
with open("Q4/Admin/AnswerKey.txt","r") as f:
    for i in f.readlines():
        l=i.split()
        ans_key[int(l[0])]=l[1]

s=''            
for student in students:
    marks=0
    student_key={}
    name=student+'_'+str(students[student])+'.txt'
    with open(f"Q4/Student/{name}") as f:
        for data in f.readlines():
            l=data.split()
            student_key[int(l[0])]=l[1]
            
    for qno in student_key:
        if student_key[qno]==ans_key[qno]:
            marks+=4
        elif student_key[qno]=='-':
            marks+=0
        elif student_key[qno]!=ans_key[qno]:
            marks-=1

    s+=student+' '+str(students[student])+' '+str(marks)+'\n'

with open("FinalReport.txt","w") as file:
    file.write(s)
    print("Final Report created successfully")

        
            
