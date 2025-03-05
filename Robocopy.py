import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import shutil
import os

def get_drive_info(path):
    """Gets total size and free space of the drive where the path is located."""
    if os.path.exists(path):
        total, used, free = shutil.disk_usage(path)
        return f"Total: {total // (1024**3)} GB, Free: {free // (1024**3)} GB"
    return "Invalid Path"

def select_source():
    folder = filedialog.askdirectory()
    if folder:
        source_var.set(folder)
        source_info_var.set(get_drive_info(folder))

def select_destination():
    folder = filedialog.askdirectory()
    if folder:
        destination_var.set(folder)
        destination_info_var.set(get_drive_info(folder))

def start_robocopy():
    source = source_var.get()
    destination = destination_var.get()
    
    if not source or not destination:
        messagebox.showerror("Error", "Please select both source and destination folders.")
        return
    
    robocopy_command = [
        "robocopy", source, destination, "/E", "/XC", "/XN", "/XO", "/XD", 
        "$RECYCLE.BIN", "System Volume Information", "Config.Msi", "pagefile.sys", 
        "hiberfil.sys", "swapfile.sys", "Recovery", "Windows", "ProgramData"
    ]
    
    try:
        subprocess.run(robocopy_command, shell=True)
        messagebox.showinfo("Success", "Robocopy operation completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create GUI window
root = tk.Tk()
root.title("Robocopy GUI")
root.geometry("320x240")

# Variables
source_var = tk.StringVar()
destination_var = tk.StringVar()
source_info_var = tk.StringVar()
destination_info_var = tk.StringVar()

# Source selection
tk.Label(root, text="Source Folder:").pack()
tk.Entry(root, textvariable=source_var, width=30).pack()
tk.Button(root, text="Browse", command=select_source).pack()
tk.Label(root, textvariable=source_info_var, fg="blue").pack()

# Destination selection
tk.Label(root, text="Destination Folder:").pack()
tk.Entry(root, textvariable=destination_var, width=30).pack()
tk.Button(root, text="Browse", command=select_destination).pack()
tk.Label(root, textvariable=destination_info_var, fg="blue").pack()

# Start button
tk.Button(root, text="Start Robocopy", command=start_robocopy, bg="green", fg="white").pack(pady=10)

# Run the GUI
root.mainloop()
