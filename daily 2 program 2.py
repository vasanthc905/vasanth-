def checkYear(year):
    if(year%4)==0:
        if(year%100)==0:
            if(year%400)==0:
                return True
            else:
                return False
        else:
             return True
    else:
         return False
year=2001
if(checkYear(year)):
    print("leap Year")
else:
    print("not a leap Year")
            


          
