import tkinter as tk
from tkinter import messagebox

tasks = []
task_number = 1

def add_task():
    global task_number
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, f"{task_number}. {task}")
        entry.delete(0, tk.END)
        task_number += 1

def edit_task():
    selected_index = listbox.curselection()
    if selected_index:
        selected_task = listbox.get(selected_index)
        new_task = entry.get()
        if new_task:
            tasks[selected_index[0]] = new_task
            listbox.delete(selected_index)
            listbox.insert(selected_index, f"{selected_task.split('.')[0]}. {new_task}")
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")

def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        confirmation = messagebox.askyesno("Confirm", "Are you sure you want to delete the selected task?")
        if confirmation:
            listbox.delete(selected_index)
            tasks.pop(selected_index[0])

window = tk.Tk()
window.title("Colorful To-Do List")


listbox = tk.Listbox(window, width=50, bg="grey", fg="black")
listbox.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12), width=35)
entry.pack(pady=10)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add", bg="green", fg="white", command=add_task)
add_button.grid(row=0, column=0, padx=5)

edit_button = tk.Button(button_frame, text="Edit", bg="orange", fg="white", command=edit_task)
edit_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete", bg="red", fg="white", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

window.mainloop()