name="priya sharma"
product="Wireless Headphones"
price=2499.0
quantity=2
GST_per=18.0
Charge=99.0

total_price=price*quantity
gst_amount=total_price*GST_per/100
final_bill=total_price+gst_amount+Charge

print("\t\t\tSHOOPMART ONLINE")
print(f"\t\t\t{" "*4}-------")
print(f"\t\t\t{" "*4}Invoice")
print(f"Customer  Name\t:{" "*4}{name}")
print(f"Invoice Number\t:{" "*4}INV2025220502")
print(f"Invoice Date\t:{" "*4}20 May 2025")
print("\n")
print(f"{product}{" "*8}PRICE{" "*8}QUANTITY{" "*8}TOTAL(INR)")
print(f"PRODUCT DETIALS{" "*12}{price}{" "*10}{quantity}{" "*13}{total_price:,.2f}")
print("----------------------------------------------------------------------------------")

print(f"Total Price {" "*34}:{" "*10}{total_price:,.2f}")
print(f"GST(18%) {" "*37}:{" "*10}{gst_amount:,.2f}")
print(f"Delivery Charge {" "*30}:{" "*10}{Charge:,.2f}")
print("----------------------------------------------------------------------------------")
print(f"Final Bill Amount {" "*28}:{" "*10}{final_bill:,.2f}")
print("\n")
print("\t\t\t\tThank you for shopping with ShopSmart!")


