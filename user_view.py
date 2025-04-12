import tkinter as tk
from tkinter import messagebox
from auth import authenticate

def login():
    username = username_entry.get()
    password = password_entry.get()

    if authenticate(username, password):
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
       messagebox.showerror("Login Failed", "Invalid username or password")
def main():
    root = tk.Tk()
    root.title("User view")
    root.geometry("600x800")

    frame = tk.Frame(root)
    frame.pack(expand = True)

    tk.Label(frame, text="Username:").pack(pady=5)
    global username_entry
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)

    tk.Label(frame, text="password:").pack(pady=5)
    global password_entry
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=5)

    tk.Button(frame, text="Login", command=login).pack(pady=10)

    root.mainloop()
if __name__ == "__main__":
     main()