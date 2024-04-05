from pyhpc.utils.SSHSession import SSHSession

class HPCController:
    session: SSHSession = None
    
    def __init__(self, session: SSHSession = None):
        self.session = session
        
    def __barrier(self):
        if not self.session or not hasattr(self.session, 'client'):
            raise RuntimeWarning("Attempting to exec command when session/client not connected!")
        
    def exec_squeue(self, user: str = None):
        """Execute a command to get job statistics."""
        cmd = 'squeue'
        if user:
            cmd += f' -u {user}'
        try:
            self.__barrier()
            self.session.client.exec_command(cmd)
            stdout = self.session.client.recv(1024).decode()
            return stdout
        except Exception as e:
            print(e)