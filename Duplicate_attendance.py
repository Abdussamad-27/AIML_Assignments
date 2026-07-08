#Duplicate Attendance List

Regestration_list=["Rahul","Ravi","Rohit","Roy","Rahul","Sam","Ravi","Ram","Ankit"]

# Regestration_list before having duplicate regestrations
print("Regestration_list before having duplicate regestrations : ",Regestration_list)

#Removing duplicate Regestrations using remove()
Regestration_list.remove("Rahul")
Regestration_list.remove("Ravi")

print("Regestration_list after removing  duplicate regestrations : ",Regestration_list)


#clearing regestration list after completion of event using clear()
Regestration_list.clear()
print("Regestration_list after clearing  : ",Regestration_list)
