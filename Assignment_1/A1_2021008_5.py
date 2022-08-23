def getReverse(n):
    #since input is taken as int It automatically removes all the trailing
    #zeros before the number i.e 007 is 7 when converted to int.
    #So inverse of 007 should be 7.
    s = str(n)
    s = s[::-1]
    return(int(s))

def checkPalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False
    
def checkNarcissistic(n):
    count=0
    tot=0
    tmp=n
    s=str(n)
    l=len(s)
    while tmp>0:
        dig=tmp%10
        tmp=tmp//10
        tot+=dig**l
    if tot==n:
        return True
    else:
        return False
    
def findDigitSum(n,tot=0):
    dig=0
    while n>0:
        dig+=n%10
        n=n//10
    res=tot+dig
    if len(str(dig))>1:
        findDigitSum(dig,res)
    else:
        print(res)

def findSquareDigitSum(n,tot=0):
    sqdig=0
    while n>0:
        dig=n%10
        n=n//10
        sqdig+=dig**2
    res=tot+sqdig
    if len(str(sqdig))>1:
        findSquareDigitSum(sqdig,res)
    else:
        print(res)

ch=0
while ch<6:
    print("------------------MENU----------------")
    print("1. Find reverse of a number")
    print("2. Check whether a number is a palindrome or not.")
    print("3. Check whether a number is a Narcissistic number or not.")
    print("4. Find the sum of digits of a number")
    print("5. Find the sum of squares of digits of a number")
    print("6. Exit")
    ch=int(input("Enter choice: "))
    if ch<6:
        while True:
            n=int(input("Enter number"))
            if n>=0:
                break
    if ch==1:
        print(getReverse(n))
    elif ch==2:
        print(checkPalindrome(n))
    elif ch==3:
        print(checkNarcissistic(n))
    elif ch==4:
        findDigitSum(n)
    elif ch==5:
        findSquareDigitSum(n)


