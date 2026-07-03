#7 Employee id and badge generator

Name=input("Enter employee name :")
Department_code=input("Enter Department code:")
Joining_year=input("Enter Joining year:")
Employee_number=(input("Enter Employee number:"))
Employee_ID=Department_code+Joining_year+Employee_number

print(f"{Name} has Employee ID :{Employee_ID} ")