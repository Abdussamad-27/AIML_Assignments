#3 calculating employee attendance

days_present=int(input("Enter present days:"))
Total_working_days=int(input("Enter Total working days:"))

attendance_percentage=(days_present/Total_working_days)*100
print(f"you have attendance : {attendance_percentage:,.2f}%")
if attendance_percentage>=95:
    print("perfect attendance you will get bonus")
else:
        print("not perfect attendance you will not get bonus")


