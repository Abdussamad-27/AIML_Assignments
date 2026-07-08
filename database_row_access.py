# Tuple of tuples representing transaction records
# Format: (Transaction_ID, Customer_ID, Amount)

transactions = (
    (101, "C001", 500),
    (102, "C002", 750),
    (103, "C001", 1200),
    (104, "C003", 450),
    (105, "C001", 900),
    (106, "C002", 300)
)

# Customer ID to search
customer_id = "C001"

# Count transactions for the given customer
customer_list = ()

for record in transactions:
    customer_list += (record[1],)   # Store only Customer IDs

count = customer_list.count(customer_id)

print("Customer ID:", customer_id)
print("Number of Transactions:", count)

# Find index of a specific transaction record
search_record = (104, "C003", 450)

if search_record in transactions:
    position = transactions.index(search_record)
    print("Transaction Record Found at Index:", position)
else:
    print("Transaction Record Not Found")