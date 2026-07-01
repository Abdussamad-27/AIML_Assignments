Name="Rahul Sharma"
ID=10123
Department="Software Development"
Basic_Salary=50000.0
HRA=15000
DA=10000
TAX=7500
Gross=Basic_Salary+HRA+DA
NET=Gross-TAX


print("\t\t\t\t\t\tABC SOLLUTION PVT.LTD.")
print("\t\t\t\t\t\t----------------------")
print("\n")
print("\t\t\t\t\t\t Employee Salary Slip")
print("\n")
print(f"\tEmployee Name\t:\t{Name}\t\t\t\tDate\t:\t20 May 2025")
print(f"\tEmployee ID\t:\t{ID}\t\t\t\t\tMonth\t:\t May 2025")
print(f"\tDepartment\t:\t{Department}\t\t\t\t\t\t\t\t")
print("\n")
print("--------------------------------------------------------------------------------------------------------------------------------")
print(f"\tSalary Detials{' '*65}AMOUNT(INR)")
print(f"\tHRA{' '*76}{HRA :,.2f}")
print(f"\tDA{' '*77}{DA:,.2f}")
print(f"\tGross Salary (Basic+HRA+DA){' '*52}{Gross:,.2f}")

print(f"\tTax{' '*76}{TAX:,.2f}")
print("--------------------------------------------------------------------------------------------------------------------------------")

print(f"\tNet Salary (Gross - TAX){' '*55}{NET:,.2f}")
print("--------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\tThank you for your hardwork and dedication!")




