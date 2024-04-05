import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Application
    
class MainPage(tk.Frame):
    def __init__(self, app: "Application"):
        super().__init__(app)
        self.dispatcher = app.dispatcher
        self.app_state = app.app_state
        self.controller = app.controller
        self.subscribe()
        
        tk.Label(self, text="Main Page", font=("Arial", 20)).pack()
        tk.Button(self, text="Hamburger Menu", command=self.open_menu).pack(side="top", anchor="nw")
        tk.Label(self, text="Settings/Profile Placeholder").pack()
        
    def subscribe(self):
        self.unsubscribe_login_success = self.dispatcher.subscribe("login_success", self.on_login_success)
        self.unsubscribe_logout = self.dispatcher.subscribe("logout", self.on_logout)

    def open_menu(self):
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Option 1")
        menu.add_command(label="Option 2")
        menu.add_command(label="Logout", command=lambda: self.dispatcher.publish('logout'))
        # Positioning the menu near the button could be improved
        menu.post(10, 10)
        
    def on_login_success(self, username):
        print("Logged in user:", username)
        try:
            result = self.controller.exec_squeue()
        except Exception as e:
            print(e)
        tk.Label(self, text=result).pack()

    def on_logout(self):
        self.dispatcher.publish("show_login")

    def destroy(self):
        self.unsubscribe_login_success()
        self.unsubscribe_logout()
        super().destroy()