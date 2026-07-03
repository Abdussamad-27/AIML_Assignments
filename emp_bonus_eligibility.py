#5 calculaating employee bonus eligibility

years_of_experience=int(input("enter experience year:"))
performance_rating=float(input("enter employee performance rating :"))

if(years_of_experience>2 and performance_rating>=8):
    print("employee eligible for bonus")
else:
    print("employee not eligible for bonus")