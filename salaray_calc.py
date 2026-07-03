Name="Rahul Sharma"
ID=10123
Department="Software Development"
Basic_Salary=50000.0
HRA=15000
DA=10000
TAX=7500
Gross=Basic_Salary+HRA+DA
NET=Gross-TAX


print("\tEmployee Salary Slip")
print("\n")
print(f"\tEmployee Name\t:\t{Name}")
print(f"\tEmployee ID\t:\t{ID}")
print(f"\tDepartment\t:\t{Department}\t\t\t\t\t\t\t\t")
print("\n")
print(f"\tSalary Detials{' '*65}AMOUNT(INR)")
print(f"\tHRA{' '*76}{HRA :,.2f}")
print(f"\tDA{' '*77}{DA:,.2f}")
print(f"\tGross Salary (Basic+HRA+DA){' '*52}{Gross:,.2f}")

print(f"\tTax{' '*76}{TAX:,.2f}")

print(f"\tNet Salary (Gross - TAX){' '*55}{NET:,.2f}")
