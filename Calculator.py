import tkinter as tk
import math

def on_click(event):
    current_text = display.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif button_text == "C":
        display.set("")
    elif button_text == "√":
        try:
            result = math.sqrt(float(current_text))
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif button_text == "x!":
        try:
            result = math.factorial(int(current_text))
            display.set(result)
        except Exception as e:
            display.set("Error")
    else:
        display.set(current_text + button_text)

window = tk.Tk()
window.title("Colorful Calculator")
window.geometry("300x400")

# Calculator heading
heading_label = tk.Label(window, text="Calculator", font=("Arial", 20, "bold"), pady=10)
heading_label.pack()

# Display for the calculator
display = tk.StringVar()
display.set("")
display_entry = tk.Entry(window, textvariable=display, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
display_entry.pack(fill=tk.BOTH, padx=10, pady=10, ipadx=5, ipady=5)

# Calculator buttons
button_frame = tk.Frame(window)
button_frame.pack()

buttons = [
    ('7', '8', '9', '/', '√'),
    ('4', '5', '6', '*', 'x!'),
    ('1', '2', '3', '-', 'C'),
    ('0', '.', '=', '+', '')
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(button_frame, text=text, font=("Arial", 15, "bold"), padx=10, pady=10, bd=5, relief=tk.RIDGE)
        button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
        button.bind("<Button-1>", on_click)

button_frame.columnconfigure(4, weight=1)
button_frame.rowconfigure(4, weight=1)

window.mainloop()