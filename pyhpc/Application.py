import tkinter as tk
from pyhpc.pages import *
from pyhpc.utils.EventDispatcher import EventDispatcher
from pyhpc.state.AppState import AppState
from pyhpc.controllers.HpcController import HPCController

class Application(tk.Tk):
    
    frames: dict[tk.Frame, tk.Frame] = {}
    current_frame: tk.Frame = None
    
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("HPC")
        self.app_state = AppState()
        self.dispatcher = EventDispatcher()
        self.controller = HPCController()
        
        self.dispatcher.subscribe("login_success", lambda username: self.show_frame(MainPage))
        self.dispatcher.subscribe("logout", lambda: self.show_frame(LoginPage))
        self.dispatcher.subscribe("show_login", lambda: self.show_frame(LoginPage))
    
        self.show_frame(LoginPage)

    def show_frame(self, container: tk.Frame):
        if container in self.frames:
            frame = self.frames[container]
            if self.current_frame is not None:
                self.current_frame.pack_forget()
            frame.pack(fill="both", expand=True)
        else:
            frame = container(self)
            self.frames[container] = frame
            if self.current_frame is not None:
                self.current_frame.pack_forget()
            frame.pack(fill="both", expand=True)

        self.current_frame = frame
