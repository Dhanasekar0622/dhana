import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")

        # Task list
        self.tasks = []

        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        # Buttons Frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.add_button = tk.Button(
            self.buttons_frame, text="Add Task", width=12, command=self.add_task
        )
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(
            self.buttons_frame, text="Delete Task", width=12, command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Tasks Listbox
        self.tasks_listbox = tk.Listbox(root, width=35, height=15, font=("Helvetica", 12))
        self.tasks_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task.strip():
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except IndexError:
            messagebox.showerror("Error", "No task selected!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

