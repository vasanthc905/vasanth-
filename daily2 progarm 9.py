month=input("input the month9e.g. january,february etc.):")
day=int(input("input the day:"))

if month in ('january','february','march'):
    season='winter'
elif month in ('april','may','june'):
    season='spring'
elif month in ('july','august','september'):
    season='summer'
else:
    season='autum'

if(month=='march') and (day>19):
    season='spring'
elif(month=='june') and (day>20):
    season='summer'
elif(month=='september') and (day>21):
    season='autum'
elif(month=='december') and (day>20):
    season='winter'

print("season is ",season)
