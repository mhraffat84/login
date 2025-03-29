tasks=[] # to create empty list

def show_tasks():
    print("\n Your Task List:")
    print("---------------")
    for i, task in enumerate(tasks, start=1):   
        print(f"{i}. {task}") # to show the tasks in numeric order
    
    print("\n")

while True:
    print("-------------------------------")
    print("//////Welcome to the To-Do List App\\\\\\") # to show the message
    print("-------------------------------")
    action = input(" (add / view / exit):").lower() # to take input from user

    if action == "add": # to add task
        task= input("Enter the task: ") # to take input from user
        tasks.append(task) # to add the task to the list
    
    elif action == "view": # to view the task
        show_tasks()
    
    elif action == "exit": # to exit the program
        print("Exiting. Goodbye!")
        print("                  ")
        break
    else:
        print("Invalid Input. Please try again") # to show the message if the input is invalid

