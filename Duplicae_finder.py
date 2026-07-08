#Inventory duplicate finder

product_codes=["9j","cv9","cb34","ok9","ii9","cv9","cv9", "jk90","cv9", ]

print("Product codes : ",product_codes)

#counting repeated product code using count
cv9_count=product_codes.count("cv9")
print(f"code cv9 repeated for {cv9_count}  times.")
#finding first occurance code using 
cv9_firstOccurance=product_codes.index("cv9")
print(f"code cv9 presented at position {cv9_firstOccurance}.")

user_input=input("Enter code check how many time it is repeated:")

if user_input in product_codes:
    count1=product_codes.count(user_input)
    print(f"{user_input} repeated for {count1} times")