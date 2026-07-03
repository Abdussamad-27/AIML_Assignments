#profit and loss statement

revenue=float(input("Enter your revenue:"))
expenses=float(input("Enter your expenses:"))

profit_loss=revenue-expenses

if profit_loss>0:
    print("Company made profit")
elif profit_loss<0:
     print("Company made loss")
else:
     print("Break even")