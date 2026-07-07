#hospital patient information card


Patient_Name=input("Enter Patient Name:")
Age=int(input("Enter Age:"))
Gender=input("Enter Gender:")
Blood_Group=input("Enter Blood Group:")
Wieght=float(input("Enter Weight:"))
Height=float(input("Enter Height:"))
Consulation_Fee=float(input("Enter Consulation Fee:"))
Regestration_Fee=float(input("Enter Regestration Fee:"))

#calculating total amount to pay

Total_Amount_Payable=Consulation_Fee+Regestration_Fee
#displaying information card
print("\n")
print("\t\t\tCITY CARE HOSPITAL")
print("\t\t\tPatienet Information card")
print("----------------------------------------------------------------------------------")

print(f"Patient Name{" "*12}:{" "*2}{Patient_Name}")
print(f"Age{" "*21}:{" "*2}{Age}")

print(f"Gender{" "*18}:{" "*2}{Gender}")

print(f"Blood Group{" "*13}:{" "*2}{Blood_Group}")

print(f"Wieght{" "*18}:{" "*2}{Wieght}")

print(f"Height{" "*18}:{" "*2}{Height}")
print(f"Consulation Fee{" "*9}:{" "*2}{Consulation_Fee}")
print(f"Regestration Fee{" "*8}:{" "*2}{Regestration_Fee}")
print("----------------------------------------------------------------------------------")
print(f"Total Amount Payable{" "*4}:{" "*2}{Total_Amount_Payable}")











