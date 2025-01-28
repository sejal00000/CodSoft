import os

tasks = {}
clear = lambda:os.system('cls')
def create(tasks):
    clear()
    print("--- Add Task ---")
    while True:
        a = input("\nEnter Task: ")
        tasks[a] = "Incomplete"        
        while True:
          b = input("Add Another Task? (y/n): ")
          if b.lower() == "n":
            return
          elif b.lower() == "y":
            break
          elif b.lower() != "n":
            print("Invalid Input")
             
def view_tasks(tasks):
    clear()
    if not tasks:
        print("No Task Has Been Added\n")
    else:
        print("--- To Do List ---\n")
        i = 1
        for key,value, in tasks.items():
            print(f"{i}. {key}  [{value}]")
            i += 1
       
def update(tasks):
    while True:
        if all(value == "Completed" for value in tasks.values()):
            clear()
            print("All tasks are complete\n")
            return
    
        print("--- Marking Incomplete Task ---\n")
        view_tasks(tasks)
        a = input("\nEnter Number To Update:- ")
        
        try:
            i = 1
            for key in tasks:
                if int(a) == i:
                    tasks[key] = "Completed"
                    view_tasks(tasks)
                    break
                i +=1 
            
            else:
                print("Invalid Number\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            
        
            
        while True:
            b = input("Mark Another Task? (y/n): ")
            if b.lower() == "n":
                return
            elif b.lower() == "y":
                break
            elif b.lower() != "n":
                print("Invalid Input")
            
def delete_task(tasks):
    clear()
    print("\n--- Delete Task ---\n")
    view_tasks(tasks)
    a = int(input("\nEnter Task Number To Delete:"))
    i = 1
    for key in tasks.keys():
        if a== i:
            removed_value = tasks.pop(key)  
            print(f"Deleted task: {a}\n")
            break        
        i +=1
    else:
        print("Invalid Task Number")
    while True:
        b = input("Delete Another Task? (y/n): ")
        if b.lower() == "n":
            return
        elif b.lower() == "y":
            break
        elif b.lower() != "n":
            print("Invalid Input")
         
        
def menu():
    while True:
        print("\n ---- To-Do List ----\n")
        print("1. Add Task")
        print("2. Display Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        try:
            choice = int(input("\nChoose Option: "))
        except ValueError:
            print("Invalid Input\n")
            continue
        
        if choice == 1:
            create(tasks)
        if choice == 2:
            view_tasks(tasks)
        if choice == 3:
            update(tasks)
        if choice == 4:
            delete_task(tasks)
        if choice == 5:
            break
        if choice >= 5:
            print("invalid choice!! \n")
            
menu()