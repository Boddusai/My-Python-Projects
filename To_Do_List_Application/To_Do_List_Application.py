def task():
    tasks = []  # Initialize empty list
    
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")
    
    try:
        total_task = int(input("Enter how many tasks you want to add = "))
        
        for i in range(1, total_task + 1):
            task_name = input(f"Enter task {i} = ")
            tasks.append(task_name)
            
        print("\nToday's Tasks Are:")
        for t in tasks:
            print("-", t)
            
    except ValueError:
        print("Please enter a valid number.")
        return

    # Menu Loop
    while True:
        try:
            print("\nChoose Operation:")
            operation = int(input("1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\nEnter your choice = "))
            
            if operation == 1:
                add = input("Enter task you want to add = ")
                tasks.append(add)
                print(f"Task '{add}' added successfully.")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update = ")
                if updated_val in tasks:
                    update = input("Enter new task name = ")
                    ind = tasks.index(updated_val)
                    tasks[ind] = update
                    print(f"Task '{updated_val}' updated to '{update}'.")
                else:
                    print("Task not found.")

            elif operation == 3:
                del_val = input("Enter task you want to delete = ")
                if del_val in tasks:
                    tasks.remove(del_val)
                    print(f"Task '{del_val}' deleted successfully.")
                else:
                    print("Task not found.")

            elif operation == 4:
                if len(tasks) == 0:
                    print("No tasks available.")
                else:
                    print("\nYour Current Tasks:")
                    for i, t in enumerate(tasks, start=1):
                        print(f"{i}. {t}")

            elif operation == 5:
                print("Closing the program.... Thank You")
                break

            else:
                print("Invalid Input. Please enter a number from 1 to 5.")

        except ValueError:
            print("Invalid Input. Please enter a valid number.")

task()