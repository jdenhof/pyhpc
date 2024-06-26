import tkinter as tk
from tkinter import messagebox
from pyhpc.utils.SSHSession import SSHSession
from typing import TYPE_CHECKING
import pyhpc.secrets as secrets

if TYPE_CHECKING:
    from main import Application

class LoginPage(tk.Frame):
    def __init__(self, app: "Application"):
        super().__init__(app)
        self.dispatcher = app.dispatcher
        self.app_state = app.app_state
        self.controller = app.controller
        
        self.host_name = tk.StringVar(value=secrets.HOST)
        self.port = tk.StringVar(value=secrets.PORT)
        self.username = tk.StringVar(value=secrets.USERNAME)
        self.password = tk.StringVar(value=secrets.PASSWORD)

        tk.Label(self, text="Username:").pack()
        tk.Entry(self, textvariable=self.username).pack()

        tk.Label(self, text="Password:").pack()
        tk.Entry(self, textvariable=self.password, show="*").pack()
        
        tk.Label(self, text="Host").pack()
        tk.Entry(self, textvariable=self.host_name).pack()
        tk.Label(self, text="Port").pack()
        tk.Entry(self, textvariable=self.port).pack()

        tk.Button(self, text="Login", command=self.check_login).pack()

    def check_login(self):
        try:
            self.controller.session = SSHSession(
                self.host_name.get(),
                self.port.get(),
                self.username.get(),
                self.password.get()
            )
            self.dispatcher.publish('login_success', self.username.get())
        except Exception as e:
            messagebox.showerror("Login failed", f"Incorrect username or password, {e}")
