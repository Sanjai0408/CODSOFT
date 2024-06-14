import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation
        
        all_characters = lowercase_letters + uppercase_letters + digits + special_characters
        
        password = ''.join(random.choice(all_characters) for _ in range(length))
        
        password_label.config(text="Generated Password: " + password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


window = tk.Tk()
window.title("Password Generator")

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.configure(bg="#080399")

length_label = tk.Label(window, text="Enter Length:", font=('Arial', 12, 'bold'),bg="#080399", fg="white")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

generate_button = tk.Button(window, text="Generate Password", command=generate_password,bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'))
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_label = tk.Label(window, text="", font=('Arial', 14),bg="#080399", fg="white")
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
