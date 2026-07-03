#6 calculating product price with tax % and dicount %

product_price=float(input("Enter product price : "))
tax_percentage=float(input("Enter tax % : "))
discount_percentage=float(input("Enter discount % : "))
#calculating discount_amount
discount_amount=product_price*(discount_percentage/100)
price_after_discount=product_price-discount_amount

#calculating tax_amount
tax_amount=price_after_discount*(tax_percentage/100)
#calculating final amount
final_product_price=price_after_discount+tax_amount

print(f"You have to pay Final Price : {final_product_price:,.2f}")