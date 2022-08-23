def noteCreate():
    notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C"]     
    
    with open("scaleMajor.txt","w") as f:
        mj=''
        major=[["C","D","E","F","G","A","B","C'"],
               ["C#","D#","F","F#","G#","A#","C","C#'"],
               ["D","E","F#","G","A","B","C#","D'"],
               ["D#","F","G","G#","A#","C","D","D#'"],
               ["E","F#","G#","A","B","C#","D#","E'"],
               ["F","G","A","A#","C","D","E","F'"],
               ["F#","G#","A#","B","C#","D#","F","F#'"],
               ["G","A","B","C","D","E","F#","G'"],
               ["G#","A#","C","C#","D#","F","G","G#'"],
               ["A","B","C#","D","E","F#","G#","A'"],
               ["A#","C","D","D#","F","G","A","A#'"],
               ["B","C#","D#","E","F#","G#","A#","B'"]]
        for i in major:
            mj+=' '.join(i)+'\n'
        f.write(mj)
        
    with open("scaleMinor.txt","w") as fp:
        mn=''
        minor=[["C","D","D#","F","G","G#","A#","C'"],
               ["C#","D#","E","F#","G#","A","B","C#'"],
               ["D","E","F","G","A","A#","C","D'"],
               ["D#","F","F#","G#","A#","B","C#","D#'"],
               ["E","F#","G","A","B","C","D","E'"],
               ["F","G","G#","A#","C","C#","D#","F'"],
               ["F#","G#","A","B","C#","D","E","F#'"],
               ["G","A","A#","C","D","D#","F","G'"],
               ["G#","A#","B","C#","D#","E","F#","G#'"],
               ["A","B","C","D","E","F","G","A'"],
               ["A#","C","C#","D#","F","F#","G#","A#'"],
               ["B","C#","D","E","F#","G","A","B'"]]
        for i in minor:
            mn+=' '.join(i)+'\n'
        fp.write(mn)
        
noteCreate()


def majorNotes(root):
    with open("scaleMajor.txt","r") as f:
        data=f.readlines()
        t=[]
        for i in data:
            l=[val for val in i.split()]
            t.append(l)

        for d in t:
            if d[0]==root:
                for n in d:
                    print(n,end=' ')
        
def minorNotes(root):
    with open("scaleMinor.txt","r") as fl:
        data=fl.readlines()
        t=[]
        for i in data:
            l=[val for val in i.split()]
            t.append(l)

        for d in t:
            if d[0]==root:
                for n in d:
                    print(n,end=' ')
                    

root=input("Enter the root note: ")
scale=input("Enter the type of scale (Minor/Major): ")
if scale=='Major':
    minorNotes(root)
elif scale=='Minor':
    minorNotes(root)
else:
    print("Wrong Scale")

