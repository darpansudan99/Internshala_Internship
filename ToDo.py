class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['description']} {'(Completed)' if task['completed'] else ''}")

    def add_task(self, description):
        task = {'description': description, 'completed': False}
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task['description']}' deleted.")
        else:
            print("Invalid task index.")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '3':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '4':
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(index)
        elif choice == '5':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
