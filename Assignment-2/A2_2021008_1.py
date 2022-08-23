def wordcount(word):
    count=0
    with open('question1_input.txt','r') as f:
        for i in f.read().split():
            if i.lower()==word.lower():
                count+=1
        if count==0:
            print("Word does not exist")
        else:
            print("Word count: ",count)

def uniquewords():
    with open('question1_input.txt','r') as f:
        s=set()
        for i in f.read().split():
            s.add(i)
        for word in s:
            print(word,end=' ; ')
            

def uniquewordcounts():
    with open('question1_input.txt','r') as f:
        d={}
        for i in f.read().split():
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        print("Word count:")
        for word in d:
            print(word,' : ',d[word])
    
def replaceword(word,new):
    with open('question1_input.txt','r') as f:
        x=''        
        for i in f.readlines():
            for w in i.split():
                if w==word:
                    x+=new+' '
                else:
                    x+=w+' '
            x+='\n'
    with open('question1_input.txt','w') as file:
        file.write(x)
        print('Replaced Successfully')

ch=0
while ch<5:
    print("Enter your choice:")
    print("1. Display specific word count")
    print("2. Display all unique words")
    print("3. Display all word counts")
    print("4. Replace word")
    print("5. Quit")
    ch=int(input("Enter choice: "))
    if ch==1:
        word=input("Enter word: ")
        wordcount(word)
    elif ch==2:
        uniquewords()        
    elif ch==3:
        uniquewordcounts()
    elif ch==4:
        word=input("Enter word you want to replace: ")
        new=input("Enter new word:")
        replaceword(word,new)
        
