Student_Name="Arjun Verma"
Student_ID=20250078

Course_Name="python programming"

Duration="3 Months"
Email="arjunverma@gmail.com"
Mobile_number="+91 9876543210"
Course_Fee=15000.0
Registration_Fee=2000.0

#calcuclating remaining fee

Remaining_Fee=Course_Fee-Registration_Fee

print("\t\t\tBRIGHT FUTURE INSTITUTE")
print(f"\t\t\t{" "*4}----------------")
print(f"\t\t\t{" "*4}Regestration Recipt")
print("----------------------------------------------------------------------------------")

print(f"Student Name{" "*4}:{" "*2}{Student_Name}")
print(f"Student ID{" "*6}:{" "*2}{Student_ID}")
print(f"Course Name{" "*5}:{" "*2}{Course_Name}")

print(f"Duration{" "*8}:{" "*2}{Duration}")
print(f"Email{" "*11}:{" "*2}{Email}")


print(f"Mobile Number{" "*3}:{" "*2}{Mobile_number}")

print(f"Course Fee{" "*6}:{" "*2}{Course_Fee:,.2f}")

print(f"Registration Fee:{" "*2}{Registration_Fee:,.2f}")



print("----------------------------------------------------------------------------------")
print(f"Remaining Fee{" "*3}:{" "*2}{Remaining_Fee:,.2f}")
print("\n")
print("\t\t\t\tWelcome to Bright Future Institute!")


