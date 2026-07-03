#9 Company budget allocation checker

budget_amount=float(input("Enter budget amount : "))
allocated_budget=float(input("Enter allocated budget amount : "))
department_performance=float(input("Enter department performance : "))

#checking approval status
approval_status=budget_amount<=allocated_budget and department_performance>=7#logical and  comparission operator


if approval_status:
    print("budget status approved")
else:
    print("budget status denied")




