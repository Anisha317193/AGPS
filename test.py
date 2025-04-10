import tkinter as tk
from tkinter import messagebox
#login function
def login():
    username = username_entry.get()
    password = password_entry.get()
    try:
        with open("users.txt", "r") as file:
...             for line in file:
...               stored_user, stored_pass = line.strip().split(",")
...               if username == stored_user and password == stored_pass:
...                   messagebox.showinfo("Login Successful", f"welcome, {username}!")
...                   return
...               messagebox.showerror("Login Successful", "Invalid username or password.")
...     except FileNotFoundError:
...         messagebox.showerror("Error", "User data file not found.")
... 
...     #Main GUI function
... def main():
...     global username_entry, password_entry
...     root = tk.TK()
...     root.title("user view")
...     root.geometry("600x800") 
...     #create a frame to center elements
...     frame = tk.Frame(root)
...     frame.pack(expand=True)
... 
...     #Username label and entry
...     tk.Label(frame, text="Username:").pack(pady=5)
...     global username_entry
...     username_entry = tk.Entry(frame)
...     username_entry.pack(pady=5)
... 
...     #Password label and entry
...     tk.label(frame, text="Password:").paack(pady=5)
...     global password_entry
...     password_entry = tk.Entry(frame, shoe="*")
...     password_entry.pack(paddy=5)
... 
...     #Login button
...     tk.Button(frame, text="Login", command=login).pack(pady=10)
... 
...     root.mainloop()
...     #Entery point
...     if __name__ == "__main__":
