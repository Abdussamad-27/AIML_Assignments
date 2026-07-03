#8 OverTime pay calculator

standard_hours=8
hours_worked=int(input("Enter total worked hours: "))
hourly_rate=float(input("Enter hourly rate amount:"))
overtime_worked=hours_worked-standard_hours

#Calculating OverTime pay 
overpay=overtime_worked*hourly_rate*1.5

print(f"The employee over time work hours is  : {overtime_worked}")
print(f"The amount to pay for over time is : {overpay}")