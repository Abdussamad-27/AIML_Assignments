#10 employee  age_eligibility_for_retirement plan

eligible=int(input("Enter retirement age : "))
age=int(input("Enter employee age : "))
#checking eligibility
if age>=eligible:
    print("emplloyee is eligible for company's retirement plan.")
else:
    print("employee is not  eligible for company's retirement plan.")