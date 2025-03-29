Tasks=[]

while True:
  task=input("Enter a task to add or enter (Exit) to quit: ")
  if task.lower() == "exit":
    break
  Tasks.append(task)
  
print("Your Tasks List are:")
for i, task in enumerate(Tasks, start=1):
    print(f"{i}. {task}")

print("Goodbye!")