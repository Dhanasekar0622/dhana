import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Contact book data
contacts = {}

# Functions
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone:
        contacts[name] = {"phone": phone, "email": email}
        update_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Contact '{name}' added!")
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, name)

def view_contact():
    try:
        selected_contact = contact_list.get(contact_list.curselection())
        details = contacts[selected_contact]
        messagebox.showinfo("Contact Details", 
                            f"Name: {selected_contact}\nPhone: {details['phone']}\nEmail: {details['email']}")
    except:
        messagebox.showwarning("Selection Error", "Please select a contact to view!")

def delete_contact():
    try:
        selected_contact = contact_list.get(contact_list.curselection())
        del contacts[selected_contact]
        update_contact_list()
        messagebox.showinfo("Deleted", f"Contact '{selected_contact}' has been deleted.")
    except:
        messagebox.showwarning("Selection Error", "Please select a contact to delete!")

def update_contact():
    try:
        selected_contact = contact_list.get(contact_list.curselection())
        new_phone = simpledialog.askstring("Update Phone", f"Enter new phone for {selected_contact}:")
        new_email = simpledialog.askstring("Update Email", f"Enter new email for {selected_contact}:")
        if new_phone:
            contacts[selected_contact]["phone"] = new_phone
        if new_email:
            contacts[selected_contact]["email"] = new_email
        update_contact_list()
        messagebox.showinfo("Updated", f"Contact '{selected_contact}' updated.")
    except:
        messagebox.showwarning("Selection Error", "Please select a contact to update!")

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

# Input Fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contact", command=view_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Contact List
tk.Label(root, text="Contacts").pack()
contact_list = tk.Listbox(root)
contact_list.pack(expand=True, fill=tk.BOTH)

# Start the application
root.mainloop()
