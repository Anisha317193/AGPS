import pandas as pd
import os
import sys

USERS_FILE = "data/users.csv"
PASSWORD_FILE = "data/passwords.csv"

def initialize_file():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(USERS_FILE):
        pd.DataFrame(columns=["ID", "Name", "Username", "Password", "Email", "Role"]).to_csv(USERS_FILE, index=False)
    if not os.path.exists(PASSWORD_FILE):
        pd.DataFrame(columns=["Username", "Password", "Role"]).to_csv(PASSWORD_FILE, index=False)

def authenticate(username, password):
    try:
        df = pd.read_csv(PASSWORD_FILE)
        user = df[(df['Username'] == username) & (df['Password'] == password)]
        if not user.empty:
            return user.iloc[0]['Role']
    except FileNotFoundError:
        pass
    return None

def add_user():
    print("\n➕ Add New User")
    role = input("Role (admin/student): ").strip().lower()
    user_id = input("ID: ").strip()
    name = input("Full Name: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    email = input("Email: ").strip()

    if not all([user_id, name, username, password, email, role]):
        print("❌ Error: All fields are required.\n")
        return

    users_df = pd.read_csv(USERS_FILE)
    if user_id in users_df['ID'].astype(str).values or username in users_df['Username'].values:
        print("❌ Error: ID or Username already exists.\n")
        return

    new_user = pd.DataFrame([{
        "ID": user_id,
        "Name": name,
        "Username": username,
        "Password": password,
        "Email": email,
        "Role": role
    }])
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    users_df.to_csv(USERS_FILE, index=False)

    # Add to password file
    pwd_df = pd.read_csv(PASSWORD_FILE)
    new_pwd = pd.DataFrame([{"Username": username, "Password": password, "Role": role}])
    pwd_df = pd.concat([pwd_df, new_pwd], ignore_index=True)
    pwd_df.to_csv(PASSWORD_FILE, index=False)

    print(f"✅ {role.capitalize()} added successfully!\n")

def remove_student():
    user_id = input("Enter Student ID to remove: ").strip()
    users_df = pd.read_csv(USERS_FILE)
    if user_id not in users_df['ID'].astype(str).values:
        print("❌ Student ID not found.")
        return

    username = users_df.loc[users_df['ID'].astype(str) == user_id, 'Username'].values[0]
    users_df = users_df[users_df['ID'].astype(str) != user_id]
    users_df.to_csv(USERS_FILE, index=False)

    pwd_df = pd.read_csv(PASSWORD_FILE)
    pwd_df = pwd_df[pwd_df['Username'] != username]
    pwd_df.to_csv(PASSWORD_FILE, index=False)

    print("✅ Student removed successfully!\n")

def view_students():
    users_df = pd.read_csv(USERS_FILE)
    students = users_df[users_df['Role'] == 'student']
    if students.empty:
        print("No students found.\n")
    else:
        print("\n📄 All Students Information:\n")
        print(students[['ID', 'Name', 'Username', 'Email']].to_string(index=False))
        print()

def view_own_profile(username):
    users_df = pd.read_csv(USERS_FILE)
    student = users_df[users_df['Username'] == username]
    if not student.empty:
        print("\n👤 Your Profile:\n")
        print(student[['ID', 'Name', 'Username', 'Email', 'Role']].to_string(index=False))
        print()
    else:
        print("❌ Profile not found.")

def admin_panel():
    while True:
        print("\n📋 Admin Panel")
        print("1. Add User")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            view_students()
        elif choice == '4':
            print("👋 Logged out.\n")
            break
        else:
            print("❗ Invalid option.\n")

def student_panel(username):
    while True:
        print("\n🎓 Student Panel")
        print("1. View My Profile")
        print("2. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            view_own_profile(username)
        elif choice == '2':
            print("👋 Logged out.\n")
            break
        else:
            print("❗ Invalid option.\n")

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    role = authenticate(username, password)
    if role == 'admin':
        print(f"\n✅ Welcome Admin: {username}")
        admin_panel()
    elif role == 'student':
        print(f"\n✅ Welcome Student: {username}")
        student_panel(username)
    else:
        print("❌ Invalid credentials.")

def main():
    initialize_file()
    while True:
        print("\n==== Student Management System ====")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            login()
        elif choice == '2':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice.\n")

if __name__ == "__main__":
    main()