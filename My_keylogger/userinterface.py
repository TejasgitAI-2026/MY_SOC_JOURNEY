import psutil
import tkinter as tk
from tkinter import ttk
import os
# Suspicious keywords
suspicious_keywords = [
    "pynput",
    "keyboard",
    "pyhook",
    "listener",
    "keylog"
]

# Function to scan processes
def scan_processes():

    for row in tree.get_children():
        tree.delete(row)

    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline_list = process.info['cmdline']

            if not cmdline_list:
                continue

            full_cmd = " ".join(cmdline_list).lower()

            file_name = os.path.basename(cmdline_list[-1])

            for keyword in suspicious_keywords:
                if keyword in full_cmd:

                    tree.insert(
                        "",
                        "end",
                        values=(
                            process.info['name'],
                            process.info['pid'],
                            file_name,
                            "HIGH RISK"
                        )
                    )

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue


# Create window
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Keylogger Detection Dashboard")
root.geometry("1000x800")
root.configure(bg="#0a0a0f")   # Purple-black background

# Title label
title = tk.Label(
    root,
    text="🔐 Keylogger Detector",
    font=("Arial", 22, "bold"),
    fg="#a855f7",      # Neon purple
    bg="#0a0a0f"
)
title.pack(pady=15)

# Scan button
scan_button = tk.Button(
    root,
    text="🔍 Scan Maadi",
    font=("Arial", 12, "bold"),
    bg="#7c3aed",
    fg="white",
    activebackground="#9333ea",
    padx=18,
    pady=8,
    command=scan_processes
)
scan_button.pack(pady=10)

# Frame for table
frame = tk.Frame(root, bg="#0a0a0f")
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Table style
style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background="#151520",
    foreground="#e5e7eb",
    rowheight=32,
    fieldbackground="#151520",
    font=("Arial", 11)
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 12, "bold"),
    background="#1e1b2e",
    foreground="#c084fc"
)

style.map(
    "Treeview",
    background=[("selected", "#7c3aed")],
    foreground=[("selected", "white")]
)

# Table
columns = ("Process Name", "PID", "File_name", "Threat Level")

tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)

tree.pack(fill="both", expand=True)

# Run GUI
root.mainloop()