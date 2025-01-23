#To do list end of mod 1 class work


user = input("Please enter your name: ")
print(f"Welcome {user} here we are going to make a To Do List by adding, viewing, and deleting tasks!  Lets get to work! ")
# define an empty list to store tasks
tasks = []

#define a menu allowing user to input which menu option
def display_menu():
    print("\nMenu:")
    print("1. Add a Task")
    print("2. View a Task")
    print("3. Delete a Task")
    print("4. Quit")
    choice = input("Please choose 1-4 what you would like to do!")
    return choice

# # Define an empty list to store tasks


# Loop to keep the program running
while True:
    user_choice = display_menu()  # Call the display menu 

    if user_choice == "1":
        task = input("What would you like to add? ")
        tasks.append(task)
        print(f"Task {task} added!")  # Confirmation message

    elif user_choice == "2":
        if tasks:  
            print("\nYour Tasks:")
            index = 1
            for task in tasks:
                print(f"{index}, {task}") 
                index += 1
        else:
            print("No tasks to display.")  # Message if the list is empty
    
    elif user_choice == "3":
        if tasks:
            print("\nYour Tasks")
            index = 1
            for task in tasks:
                print(f"{index}, {task}")
                index += 1
                
            try:
                task_num = int(input("What number would you like to delete? :"))
                if 1 <= task_num <= len(tasks):
                    remove_task = tasks.pop(task_num - 1)
                    print(f"Task '{remove_task} has been deleted!")
                else:
                    print("invalid task number")
            except ValueError:
                print("Please enter a valid number")
        else:
            print("There are no task to delete!")
        
    elif user_choice == "4":
        print("I'll see you later! Exiting program")
        break
    else:
        print("Invalid choice, please choose between 1-4")