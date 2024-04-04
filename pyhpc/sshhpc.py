import paramiko
from tkinter import *
from tkinter import scrolledtext
import threading

class SSHHPC:
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
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(self.hostname, port=self.port, username=self.username, password=self.password)
        except Exception as e:
            print(f"Failed to connect: {e}")

    def get_job_stats(self):
        """Execute a command to get job statistics."""
        # Replace 'ls' with your HPC specific command to get job statistics
        stdin, stdout, stderr = self.client.exec_command('ls')
        return stdout.read().decode()

    def close_connection(self):
        """Close SSH connection."""
        if self.client:
            self.client.close()