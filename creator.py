import os

def choose_directory(current_directory):
    while True:
        # List the subdirectories in the current directory
        subdirectories = [name for name in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, name))]
        
        if subdirectories:
            print(f"Current directory: {current_directory}")
            print("Choose a subdirectory, or press Enter to use this directory:")
            for idx, subdir in enumerate(subdirectories, start=1):
                print(f"{idx}. {subdir}")
            folder_choice = input("Enter the number of the subdirectory, or press Enter to use this directory: ")

            if folder_choice.isdigit() and 1 <= int(folder_choice) <= len(subdirectories):
                selected_directory = subdirectories[int(folder_choice) - 1]
                current_directory = os.path.join(current_directory, selected_directory)
            elif folder_choice == "":
                return current_directory
            else:
                print("Invalid choice. Please try again.")
        else:
            print("No subdirectories found. Using this directory.")
            return current_directory

# Start at the current directory
current_directory = "."

# Allow the user to choose directories recursively
final_directory = choose_directory(current_directory)

task_count = int(input("Enter the number of tasks: "))
file_extension = input("Enter the file extension: ")
tasks_with_subtasks = input("Enter task numbers with subtasks, separated by commas (e.g., 2,3): ")
tasks_with_subtasks = [int(num.strip()) for num in tasks_with_subtasks.split(",") if num.strip().isdigit()]

subtask_end_letters = {}
for task in tasks_with_subtasks:
    last_letter = input(f"Enter the last letter of the subtask for task {task} (e.g., d): ").lower()
    subtask_end_letters[task] = last_letter

for i in range(1, task_count + 1):
    if i not in subtask_end_letters:
        file_name = os.path.join(final_directory, f"{i}.{file_extension}")
        with open(file_name, 'w') as file:
            file.write("")
        print(f"Created file: {file_name}")
    else:
        for letter in range(ord('a'), ord(subtask_end_letters[i]) + 1):
            file_name = os.path.join(final_directory, f"{i}{chr(letter)}.{file_extension}")
            with open(file_name, 'w') as file:
                file.write("")
            print(f"Created file: {file_name}")

print("All files have been created.")
