import tkinter as tk
from pages import *
from EventDispatcher import EventDispatcher


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("MPA with Frames")
    
        self.dispatcher = EventDispatcher()
        
        self.dispatcher.subscribe("login_success", lambda username: self.show_frame(MainPage))
        self.dispatcher.subscribe("logout", lambda: self.show_frame(LoginPage))
        self.dispatcher.subscribe("show_login", lambda: self.show_frame(LoginPage))
        
        self.frames = {}
        self.current_frame = None
        self.show_frame(LoginPage)

    def show_frame(self, container):
        if container in self.frames:
            frame = self.frames[container]
            if self.current_frame is not None:
                self.current_frame.pack_forget()
            frame.pack(fill="both", expand=True)
        else:
            frame = self.__initialize_container(container)
            self.frames[container] = frame
            if self.current_frame is not None:
                self.current_frame.pack_forget()
            frame.pack(fill="both", expand=True)

        self.current_frame = frame
        
    def __initialize_container(self, container):
        if container == LoginPage:
            return container(self)
        if container == MainPage:
            return container(self)
