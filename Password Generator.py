import tkinter as tk
import random
import string

def generate_password():
    name = name_entry.get()
    password_length = int(length_entry.get())
    password_complexity = complexity_var.get()

    if not name or password_length <= 0:
        password_display.config(text="Invalid input")
    else:
        characters = string.ascii_letters 
        if password_complexity == 2:
            characters += string.digits 
        elif password_complexity == 3:
            characters += string.digits + string.punctuation 

        password = ''.join(random.choice(characters) for i in range(password_length))
        password_display.config(text=password)


def accept_password():
    password = password_display.cget("text")
    name_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_display.config(text="Password accepted: " + password)

def reset_password():
    name_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_display.config(text="")

window = tk.Tk()
window.title("Colorful Password Generator")


heading_label = tk.Label(window, text="Password Generator", font=("Arial", 16, "bold"))
heading_label.pack(pady=10)


name_label = tk.Label(window, text="Enter your name:")
name_label.pack(pady=5)

name_entry = tk.Entry(window, width=30)
name_entry.pack()

length_label = tk.Label(window, text="Enter password length:")
length_label.pack(pady=5)

length_entry = tk.Entry(window, width=5)
length_entry.pack()


complexity_label = tk.Label(window, text="Select password complexity:")
complexity_label.pack(pady=5)

complexity_var = tk.IntVar()
complexity_var.set(1)

complexity_frame = tk.Frame(window)
complexity_frame.pack()

complexity_1 = tk.Radiobutton(complexity_frame, text="Alphabet Only", variable=complexity_var, value=1)
complexity_1.pack(anchor=tk.W)

complexity_2 = tk.Radiobutton(complexity_frame, text="Alphabet + Numbers", variable=complexity_var, value=2)
complexity_2.pack(anchor=tk.W)

complexity_3 = tk.Radiobutton(complexity_frame, text="Alphabet + Numbers + Symbols", variable=complexity_var, value=3)
complexity_3.pack(anchor=tk.W)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate", bg="green", fg="white", command=generate_password)
generate_button.grid(row=0, column=0, padx=5)

accept_button = tk.Button(button_frame, text="Accept", bg="blue", fg="white", command=accept_password)
accept_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="Reset", bg="red", fg="white", command=reset_password)
reset_button.grid(row=0, column=2, padx=5)


password_display = tk.Label(window, text="", font=("Arial", 12), wraplength=250, justify="center")
password_display.pack(pady=10)

window.mainloop()