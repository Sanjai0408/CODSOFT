import tkinter as tk
from tkinter import messagebox

global contacts 
contacts = {} 

def new_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    email = email_entry.get()

    details = {'phone' : phone, 'address': address, 'email' : email}

    contacts[name] = details
    messagebox.showinfo("Success", "Contact details saved successfully")
    update_listbox()

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def del_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    del contacts[selected_contact]
    messagebox.showinfo("Success", "Contact deleted successfully")
    update_listbox()

def edit_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    edit_window = tk.Toplevel()
    edit_window.title("Edit Contact")

    old_details = contacts[selected_contact]

    name_label = tk.Label(edit_window, text="Name:")
    phone_label = tk.Label(edit_window, text="Phone number:")
    address_label = tk.Label(edit_window, text="Address:")
    email_label = tk.Label(edit_window, text="Email address:")

    name_label.grid(row=0, column=0)
    phone_label.grid(row=2, column=0)
    address_label.grid(row=1, column=0)
    email_label.grid(row=3, column=0)

    name_var = tk.StringVar(value=selected_contact)
    phone_var = tk.StringVar(value=old_details['phone'])
    address_var = tk.StringVar(value=old_details['address'])
    email_var = tk.StringVar(value=old_details['email'])

    name_entry = tk.Entry(edit_window, textvariable=name_var)
    phone_entry = tk.Entry(edit_window, textvariable=phone_var)
    address_entry = tk.Entry(edit_window, textvariable=address_var)
    email_entry = tk.Entry(edit_window, textvariable=email_var)

    name_entry.grid(row=0, column=1)
    phone_entry.grid(row=1, column=1)
    address_entry.grid(row=2, column=1)
    email_entry.grid(row=3, column=1)

    def save_changes():
        new_name = name_var.get()
        new_details = {'phone' : phone_var.get(), 'address': address_var.get(), 'email' : email_var.get()}
        del contacts[selected_contact]
        contacts[new_name] = new_details
        messagebox.showinfo("Success", "Contact details updated successfully")
        edit_window.destroy()
        update_listbox()

    save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)
    save_button.grid(row=4, column=0, columnspan=2)

def view_details():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    details_window = tk.Toplevel()
    details_window.title("Contact Details")

    details_label = tk.Label(details_window, text=f"Details for {selected_contact}:")
    details_label.pack()

    details_frame = tk.Frame(details_window)
    details_frame.pack()

    for idx, (attr, value) in enumerate(contacts[selected_contact].items()):
        attr_label = tk.Label(details_frame, text=f"{attr.capitalize()}:")
        attr_label.grid(row=idx, column=0, sticky='w')
        value_label = tk.Label(details_frame, text=value)
        value_label.grid(row=idx, column=1, sticky='w')

def update_listbox():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact)

def contactBook():
    global name_entry, phone_entry,address_entry, email_entry, contact_listbox

    root = tk.Tk()
    root.title("Contact Book")

    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Name:").grid(row=0, column=0)
    tk.Label(input_frame, text="Phone number:").grid(row=1, column=0)
    tk.Label(input_frame, text="Address:").grid(row=2, column=0)
    tk.Label(input_frame, text="Email address:").grid(row=3, column=0)

    name_entry = tk.Entry(input_frame)
    phone_entry = tk.Entry(input_frame)
    address_entry = tk.Entry(input_frame)
    email_entry = tk.Entry(input_frame)

    name_entry.grid(row=0, column=1)
    phone_entry.grid(row=1, column=1)
    address_entry.grid(row=2, column=1)
    email_entry.grid(row=3, column=1)

    add_button = tk.Button(input_frame, text="Add Contact", command=new_contact)
    add_button.grid(row=4, column=0, columnspan=2, pady=5)

    contact_listbox = tk.Listbox(root)
    contact_listbox.pack(padx=10, pady=10)

    view_button = tk.Button(root, text="View Details", command=view_details)
    view_button.pack()

    edit_button = tk.Button(root, text="Edit Contact", command=edit_contact)
    edit_button.pack()

    delete_button = tk.Button(root, text="Delete Contact", command=del_contact)
    delete_button.pack()

    update_listbox()

    root.mainloop()

contactBook()
