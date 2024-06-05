import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import shutil
import os
from PIL import Image, ImageTk

def select_files(file_listbox):
    files = filedialog.askopenfilenames(title="Select Files")
    for file in files:
        file_listbox.insert(tk.END, file)

def select_folder(file_listbox):
    folder = filedialog.askdirectory(title="Select Folder")
    if folder:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_listbox.insert(tk.END, os.path.join(root, file))

def move_files(file_listbox):
    files = file_listbox.get(0, tk.END)
    if not files:
        messagebox.showerror("Error", "No files selected.")
        return

    predefined_destinations = {
        "sound": r"C:\Program Files (x86)\Steam\steamapps\common\Half-Life\cstrike\sound",
        "model": r"C:\Program Files (x86)\Steam\steamapps\common\Half-Life\cstrike\models",
        "maps": r"C:\Program Files (x86)\Steam\steamapps\common\Half-Life\cstrike\maps",
        "sprites": r"C:\Program Files (x86)\Steam\steamapps\common\Half-Life\cstrike\sprites",
        "addons": r"C:\Program Files (x86)\Steam\steamapps\common\Half-Life\cstrike\addons"
    }

    try:
        for file in files:
            file_name = os.path.basename(file).lower()
            for key in predefined_destinations:
                if key in file_name:
                    shutil.move(file, predefined_destinations[key])
                    break
            else:
                messagebox.showwarning("Warning", f"No predefined destination for file: {file}")
        messagebox.showinfo("Success", "Files moved successfully.")
        file_listbox.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to move files: {e}")

# Main application window
root = tk.Tk()
root.title("csmod")
root.geometry("335x400")
root.resizable(False, False)

# Set window icon
icon_path = r"C:\Program Files (x86)\EmuEx\BasiX\BasiX\resources\basixlogo.png"  # Replace with the path to your icon image
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

# Style configuration
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Segoe UI Symbol', 12))
style.configure('TEntry', font=('Helvetica', 12))

# Create a notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Create frames for each tab
settings_tab = ttk.Frame(notebook, padding="10 10 10 10")
move_files_tab = ttk.Frame(notebook, padding="10 10 10 10")

# Add frames to the notebook
notebook.add(move_files_tab, text='Move Files')
notebook.add(settings_tab, text='Settings')

# Settings tab content
ttk.Label(settings_tab, text="Settings", font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

# Example settings widgets
ttk.Label(settings_tab, text="Setting 1:").grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
setting1_var = tk.StringVar()
setting1_entry = ttk.Entry(settings_tab, textvariable=setting1_var)
setting1_entry.grid(row=1, column=1, pady=5, padx=5, sticky=(tk.W, tk.E))

ttk.Label(settings_tab, text="Setting 2:").grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)
setting2_var = tk.StringVar()
setting2_entry = ttk.Entry(settings_tab, textvariable=setting2_var)
setting2_entry.grid(row=2, column=1, pady=5, padx=5, sticky=(tk.W, tk.E))

# Configure the grid for the settings tab
settings_tab.columnconfigure(0, weight=1)
settings_tab.columnconfigure(1, weight=1)

# Move Files tab content
ttk.Label(move_files_tab, text="Select files or folders to move:").grid(row=0, column=0, columnspan=2, pady=10)

file_listbox = tk.Listbox(move_files_tab, selectmode=tk.MULTIPLE, width=50, height=10)
file_listbox.grid(row=1, column=0, columnspan=2, pady=10, padx=5)

select_files_button = ttk.Button(move_files_tab, text="Select Files", command=lambda: select_files(file_listbox))
select_files_button.grid(row=2, column=0, pady=10, padx=5)

select_folder_button = ttk.Button(move_files_tab, text="Select Folder", command=lambda: select_folder(file_listbox))
select_folder_button.grid(row=2, column=1, pady=10, padx=5)

move_files_button = ttk.Button(move_files_tab, text="Move Files", command=lambda: move_files(file_listbox))
move_files_button.grid(row=3, column=0, columnspan=2, pady=10, padx=5)

# Configure the grid for the move files tab
move_files_tab.columnconfigure(0, weight=1)
move_files_tab.columnconfigure(1, weight=1)

root.mainloop()
