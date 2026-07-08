# TASK 11 - LIST VS TUPLE DECISION MEMO

# Task 4: Employee Task Queue (LIST)
# A list is used because tasks can change continuesly
# We can add, remove, or update tasks whenever needed

task_queue = ["Check Emails", "Prepare Report", "Attend Meeting"]

# Adding a new task
task_queue.append("Submit Project")

print("Employee Task Queue (List):")
print(task_queue)


# Task 7: GPS Coordinate Log (TUPLE)
# A tuple is used because GPS coordinates should not change
# Tuples are immutable, making them suitable for fixed data

gps_location = (17.3850, 78.4867)   # (Latitude, Longitude)

print("\nGPS Location (Tuple):")
print(gps_location)


# Decision Memo
print("\nDecision Memo:")
print("1. List is used for the employee task queue because tasks can be added, removed, or modified.")
print("2. Tuple is used for GPS coordinates because location values should remain fixed and protected from accidental changes.")