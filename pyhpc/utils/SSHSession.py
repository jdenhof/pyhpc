import paramiko
from tkinter import *
from tkinter import scrolledtext
import threading

class SSHSession:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.client = None
        self.connect()

    def connect(self):
        """Establish SSH connection."""
        self.client = paramiko.SSHClient()
        transport = paramiko.Transport((self.hostname, int(self.port)))
        transport.connect(username=self.username)
        transport.auth_interactive(self.username, self.interactive_handler)
        self.client = transport.open_session()

    def close_connection(self):
        """Close SSH connection."""
        if self.client:
            self.client.close()
            
    def interactive_handler(self, title, instructions, prompt_list):
        """
        Handle interactive prompts in the SSH authentication process.

        - title: str, title of the interactive prompt (unused in this example)
        - instructions: str, additional instructions or information about the prompts
        - prompt_list: list of (prompt, echo) tuples, where 'prompt' is the string
                    presented by the server, and 'echo' is a bool indicating
                    whether the user input should be echoed to the screen.
        """
        responses = []
        print(title,instructions, prompt_list)
        for prompt, echo in prompt_list:
            if "password" in prompt.lower():
                # Assuming the first prompt is for a password
                responses.append(self.password)
            elif "duo two-factor" in prompt.lower() in prompt.lower():
                # If the prompt is for selecting an auth type, enter '1'
                responses.append("1")
            else:
                # Handle unexpected prompts or add more conditions as needed
                responses.append("")

        return responses