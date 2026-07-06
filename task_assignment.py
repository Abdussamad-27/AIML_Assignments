#Task Assignment Queue
#creating list for pending tasks
tasks=["designing frontend","writing code for backend","writing queries"]
print("pending tasks :",tasks)
task=tasks.pop(0)

#Assigning tasks wihch we popped from pending tasks
assigned_tasks=[task]
print("assigned tasks:",assigned_tasks)
#created a list of new tasks
new_tasks=["database connectivity","api integration","testing","deploying "]
print("New tasks : ",new_tasks)

#adding new tasks to remaining tasks

tasks.extend(new_tasks)

print(f"Pending tasks after modification :{tasks}")