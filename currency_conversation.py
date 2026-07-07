#12 Currency Conversion for International Client Billing

amount_in_inr=float(input("Enter amonut : "))
conversion_rate=float(input("Enter Convertion rate : "))#87


#calculating amount in usd 
amount_in_usd =amount_in_inr/conversion_rate

process_fee=0.02*amount_in_usd

#calculating final amount  
final_Amount=amount_in_usd+process_fee

print(f"The client has to pay :{final_Amount:,.2f}$")
