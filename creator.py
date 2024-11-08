import os

subdirectories = [name for name in os.listdir() if os.path.isdir(name)]

if subdirectories:
    print("Choose a directory to create files in:")
    for idx, subdir in enumerate(subdirectories, start=1):
        print(f"{idx}. {subdir}")
    folder_choice = input("Enter the number of the directory, or press Enter to use the current directory: ")
    if folder_choice.isdigit() and 1 <= int(folder_choice) <= len(subdirectories):
        target_directory = subdirectories[int(folder_choice) - 1]
    else:
        target_directory = "." 
else:
    target_directory = "."

task_count = int(input("Enter the number of tasks: "))
file_extension = input("Enter file extension: ")
tasks_with_subtasks = input("Enter task numbers with subtasks, separated by commas (e.g., 2,3): ")
tasks_with_subtasks = [int(num.strip()) for num in tasks_with_subtasks.split(",") if num.strip().isdigit()]

subtask_end_letters = {}
for task in tasks_with_subtasks:
    last_letter = input(f"Enter the last letter of subtask for task {task} (e.g., d): ").lower()
    subtask_end_letters[task] = last_letter

for i in range(1, task_count + 1):
    if i not in subtask_end_letters:
        file_name = os.path.join(target_directory, f"{i}.{file_extension}")
        with open(file_name, 'w') as file:
            file.write("")
        print(f"Created file: {file_name}")
    else:
        for letter in range(ord('a'), ord(subtask_end_letters[i]) + 1):
            file_name = os.path.join(target_directory, f"{i}{chr(letter)}.{file_extension}")
            with open(file_name, 'w') as file:
                file.write("")
            print(f"Created file: {file_name}")

print("All files have been created.")
