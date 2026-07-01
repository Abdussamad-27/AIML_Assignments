pin=input("Enter your pin: ")
attempts=1

while(attempts<3):
    if(pin=="1234"):
        print("Pin verified successfully!")
        break
    else:
        print("Incorrect pin. Please try again.")
        attempts+=1
        pin=input("Enter your pin: ")

if(attempts==3):
    print("Your account has been blocked.")