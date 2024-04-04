import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app)
        self.dispatcher = app.dispatcher

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self, text="Username:").pack()
        tk.Entry(self, textvariable=self.username).pack()

        tk.Label(self, text="Password:").pack()
        tk.Entry(self, textvariable=self.password, show="*").pack()

        tk.Button(self, text="Login", command=self.check_login).pack()

    def check_login(self):
        if self.username.get() == "user" and self.password.get() == "pass":
            self.dispatcher.publish('login_success', self.username.get())
        else:
            messagebox.showerror("Login failed", "Incorrect username or password")
