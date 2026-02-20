# Controls the login flow, welcome screen, and launches the quiz
import tkinter as tk
from tkinter import messagebox
from login_manager import LoginManager
from My_tkinter_app import CategoryDifficultySelector, launch_quiz



# LOGIN WINDOW 

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("EA Quiz Login")
        self.root.configure(bg="#1E90FF")  # Blue background

        self.lm = LoginManager()           # Load users.csv

        # Username label + entry
        tk.Label(root, text="Username", bg="#1E90FF", fg="white", font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(root, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        # Password label + entry
        tk.Label(root, text="Password", bg="#1E90FF", fg="white", font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        # Login button
        tk.Button(root, text="Login", font=("Arial", 12), command=self.try_login).pack(pady=10)

    # Validate login credentials
    def try_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.lm.authenticate(username, password):
            self.root.destroy()
            self.open_welcome()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    
    # WELCOME SCREEN 
    
    def open_welcome(self):
        welcome = tk.Tk()
        welcome.title("Welcome")
        welcome.configure(bg="#32CD32")  # Green background

        # Welcome message
        tk.Label(
            welcome,
            text="Welcome to the EA Hybrid Quiz!",
            bg="#32CD32",
            fg="white",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        # Continue button
        tk.Button(
            welcome,
            text="Continue",
            font=("Arial", 14),
            command=lambda: self.open_category_screen(welcome)
        ).pack(pady=20)

        welcome.mainloop()

    # Open category/difficulty selector
    def open_category_screen(self, win):
        win.destroy()
        selector_root = tk.Tk()
        CategoryDifficultySelector(selector_root, launch_quiz)
        selector_root.mainloop()



# START APP

if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()

