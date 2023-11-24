from datetime import datetime
now=datetime.now()
year=int(input("Enter year: "))
if(year>now.year):
    print("Enter correctly")
month=int(input("Enter month: "))
if (month>12):
    print("enter the month correctly")
day=int(input("Enter date: "))
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    if(day>31):
        print("Error enter correctly")
if(month==4 or month==6 or month==9 or month==11):
    if(day>30):
        print("Enter correctly")
if(month==2):
    if(year%100==0):
        if(date>28):
            print("Enter correctly")
    elif (year%4==0 or year%400==0):
        if(day>29):
            print("Enter correctly")
    else:
        if(day>28):
            print("Enter corrcetly")
birth_day=datetime(year,month,day)
def cal_age(birth_day,now):
    years=now.year-birth_day.year
    months=now.month-birth_day.month
    days=now.day-birth_day.day
    return years,months,days
age_years,age_months,age_days=cal_age(birth_day,now)
def get_days(month,year):
    if month==2:
        if (year%100 !=0 or year%4==0) and year%400==0:
            return 29
        else:
            return 28
    elif month==4 or month==6 or month==9 or month==11:
        return 30
    else:
        return 31
if age_days<0:
        age_months-=1
        age_days+= get_days(birth_day.month,birth_day.year)
if age_months<0:
    age_years-=1
    age_months+=12
diff=datetime.now()-birth_day
a=age_years*12+age_months
b=diff.days
c=b*24
m=c*60
print ("your age is",age_years,"years",age_months,"months",age_days,"days")
print("or",a,"months",age_days,"days")
print("or",b,"days")
print("or",c,"hours")
print("or",m,"minutes")

    
