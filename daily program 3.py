def sumDigitSquare(n):
    sq=o;
    while(n!=0):
        digit=n%10
        sq+=digit*digit
        n=n//10
    return sq;
def isHappy(n):
    s=set()
    s.add(n)
    while(True):
        if(n==1):
            n=sumDigitSquare(n)
        if n in s:
            return False
        s.add(n)
    return False
n=19
if(isHappy(n)):
    print("yes")
else:
    print("no")
