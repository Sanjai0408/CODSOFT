import tkinter as tk

def update_entry(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def toggle_sign():
    current_value = entry.get()
    if current_value and current_value[0] == "-":
        entry.delete(0)
    elif current_value:
        entry.insert(0, "-")
    else:
        entry.insert(tk.END, "-")

def backspace():
    current_value = entry.get()
    entry.delete(len(current_value) - 1)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("CALCULATOR")

entry = tk.Entry(root, font=('Arial', 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ('C', '⌫', '+/-', '/'),
    ('7', '8', '9', '*'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('%', '0', '.', '=')
]

for i, row in enumerate(buttons):
    for j, label in enumerate(row):
        bg_color = "#CCCCCC" if label not in ('=', 'C', '+/-', '⌫', '/', '*', '-', '+') else "#0080ff"
        command = calculate if label == '=' else clear_entry if label == 'C' else toggle_sign if label == '+/-' else backspace if label == '⌫' else percentage if label == '%' else lambda value=label: update_entry(value)
        tk.Button(root, text=label, font=('Arial', 16), padx=20, pady=20, command=command, bg=bg_color).grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
