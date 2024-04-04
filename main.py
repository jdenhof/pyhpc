import threading
from pyhpc.Application import Application


# def main():
#     hpc = SSHHPC('your_hpc_host', 22, 'your_username', 'your_password')
#     root = Tk()
#     root.title("HPC Job Statistics")

#     # Text box for displaying statistics
#     txt = scrolledtext.ScrolledText(root, undo=True)
#     txt['font'] = ('consolas', '12')
#     txt.pack(expand=True, fill='both')

#     def update_stats():
#         """Update the stats in the GUI."""
#         while True:
#             stats = hpc.get_job_stats()
#             txt.delete(1.0, END)
#             txt.insert(INSERT, stats)
#             txt.update()
#             root.after(10000, update_stats)  # Update every 10 seconds

#     # Run the update in a separate thread to avoid freezing the GUI
#     threading.Thread(target=update_stats, daemon=True).start()

#     root.mainloop()
#     hpc.close_connection()

if __name__ == "__main__":
    app = Application()
    app.mainloop()