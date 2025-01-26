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
def add_tasks():
    task = input("what would you like to add?")
    tasks.append(task) 
    print(f"Your task {task} was added to your list!")

def view_tasks():
    if tasks:
        print("\n Your Tasks:")
        for index, task in enumerate(tasks, start= 1):
            print(f"{index}. {task}")

def remove_task():
    if tasks:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):  # Display tasks with numbering
            print(f"{index}. {task}")
        
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)  # Remove the selected task
                print(f"Task '{removed_task}' has been deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("There are no tasks to delete!")  # Message if the list is empty

def quit_program():
    print("Thanks for using the To Do List program! Take care!")
    exit() #exit the program

    

# Loop to keep the program running
while True:
    user_choice = display_menu()  # Call the display menu 

    if user_choice == "1":
        add_tasks()

    elif user_choice == "2":
        view_tasks()
    
    elif user_choice == "3":
        remove_task()
    
    elif user_choice == "4":
        quit_program()
        