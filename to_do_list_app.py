import json

to_do_list = []

def save_tasks():
    with open("tasks.json" , "w") as file:
        json.dump(to_do_list , file )

def load_tasks():
    global to_do_list

    try:
        with open("tasks.json" , "r") as file:
            to_do_list = json.load(file)
    except FileNotFoundError:
        to_do_list =[]

def main():
    load_tasks()

    while (True):
        print("\nTo - Do List App")
        print("1. Add the new task: ")
        print("2. View all the task: ")
        print("3. Remove a task: ")
        print("4. Mark a task as completed: ")
        print("5. Edit the task: ")
        print("6. Exit the app")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter the valid number")
            continue
       
        if choice == 1:
            task = input("Enter the name of the task:")
            priority = input("Enter the priority(High/Medium/Low): ")
            to_do_list.append({"name" : task , "status": 'Pending' , "priority" : priority})
            print("New task added successfully!")
            save_tasks()

        elif choice == 2:
            if len(to_do_list) == 0:
                print("No task found in To-Do list")
            else:
                for index , task in enumerate(to_do_list , start = 1):
                    print(
                    f"{index}. "
                    f"Task: {task['name']} | "
                    f"Status: {task['status']} | "
                    f"Priority: {task['priority']}"
                )
            
        
        elif choice == 3:
            if len(to_do_list) == 0:
                print("No task found in To-Do list")
            else:
                for index , task in enumerate(to_do_list , start = 1):
                    print(
                    f"{index}. "
                    f"Task: {task['name']} | "
                    f"Status: {task['status']} | "
                    f"Priority: {task['priority']}"
                )
                
                index = int(input("Enter the number of the task to remove: "))

                if 1 <= index <= len(to_do_list):
                    removed_task = to_do_list.pop(index -1)
                    print(f"{removed_task['name']} , task removed successfully")
                else:
                    print("Invalid task number")
            save_tasks()

        elif choice == 4:
            if len(to_do_list) == 0:
                print("No task found in To-Do list")
            else:
                for index , task in enumerate(to_do_list , start = 1):
                    print(
                    f"{index}. "
                    f"Task: {task['name']} | "
                    f"Status: {task['status']} | "
                    f"Priority: {task['priority']}"
                )
                    
                index = int(input("Enter the number of the task to mark complete: "))

                if 1 <= index <= len(to_do_list):
                    to_do_list[index -1] ["status"] = 'Completed'
                    print("Task marked as completed")
                else:
                    print("Invalid task number")
            save_tasks()

        elif choice == 5:
            if len(to_do_list) == 0:
                print("No task found in To-Do list")
            else:
                for index , task in enumerate(to_do_list , start = 1):
                    print(
                        f"{index}. "
                        f"Task: {task['name']} | "
                        f"Status: {task['status']} | "
                        f"Priority: {task['priority']}"
                    )
                
                index =int(input("Enter the number of the task to edit: "))

                if 1 <= index <= len(to_do_list):
                    new_name = input("Enter the new task name: ")
                    new_priority = input("Enter the new priority of task(High/Medium/Low): ")

                    to_do_list[index -1]["name"] = new_name
                    to_do_list[index -1]["priority"] = new_priority
                    print("Task Updated Successfully!")
                else:
                    print("Invalid task number")
            save_tasks()

        elif choice == 6:
            print("Closing the App")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

    