#4 Inventory stock checker

current_stock=float(input("Enter current stock : "))
mininimum_threshold=float(input("Enter minimum threshold : "))
maximum_stock=float(input("Enter maximum stock : "))

if(current_stock<= mininimum_threshold ):
    print("stock is low")
elif current_stock>mininimum_threshold:
    print("STOCK IS OPTIMAL")
else:
    print("stock is overstock")
