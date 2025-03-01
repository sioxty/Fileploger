import tkinter as tk
from tkinter import filedialog, messagebox
import logging
import os
import json
from plagin import FileManager, TypeFile

PRESET_FILE = "settings/presets.json"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("FileManager")

FILE_TYPES = {
    "images": {"var": None, "entry": None, "label": "Images"},
    "documents": {"var": None, "entry": None, "label": "Documents"},
    "archives": {"var": None, "entry": None, "label": "Archives"},
    "music": {"var": None, "entry": None, "label": "Music"},
    "videos": {"var": None, "entry": None, "label": "Videos"},
}

def browse_source_dir():
    directory = filedialog.askdirectory()
    source_dir_entry.delete(0, tk.END)
    source_dir_entry.insert(0, directory)
    enable_save_button()

def browse_dest_dir(file_type):
    directory = filedialog.askdirectory()
    FILE_TYPES[file_type]["entry"].delete(0, tk.END)
    FILE_TYPES[file_type]["entry"].insert(0, directory)
    enable_save_button()

def process_files():
    source_dir = source_dir_entry.get()
    typeFile = TypeFile()
    if not source_dir:
        messagebox.showerror("Error", "Please select a source directory.")
        return

    try:
        fm = FileManager(source_dir)
        for file_type, data in FILE_TYPES.items():
            if data["var"].get():
                dest_dir = data["entry"].get()
                if dest_dir:
                    fm.move(dest_dir, typeFile.get_extensions(file_type))
                else:
                    messagebox.showerror("Error", f"Please select a destination directory for {data['label']}")
                    return

        messagebox.showinfo("Success", "Files processed successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"Source directory '{source_dir}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def save_preset():
    preset = {
        "source_dir": source_dir_entry.get(),
        **{file_type: {"dest": data["entry"].get(), "selected": data["var"].get()} for file_type, data in FILE_TYPES.items()}
    }
    try:
        with open(PRESET_FILE, "w",encoding='utf-8') as f:
            json.dump(preset, f, indent=4)
        messagebox.showinfo("Success", "Preset saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving preset: {e}")


def load_preset():
    try:
        with open(PRESET_FILE, "r") as f:
            preset = json.load(f)
            source_dir_entry.delete(0, tk.END)
            source_dir_entry.insert(0, preset["source_dir"])
            for file_type, data in FILE_TYPES.items():
                data["var"].set(preset[file_type]["selected"])
                data["entry"].delete(0, tk.END)
                data["entry"].insert(0, preset[file_type]["dest"])
        messagebox.showinfo("Success", "Preset loaded successfully!")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No preset file found.")
    except (json.JSONDecodeError, KeyError) as e:
        messagebox.showerror("Error", f"Error loading preset file: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading preset: {e}")

def enable_save_button():
    update_preset_button["state"] = "normal"

root = tk.Tk()
root.title("File Manager")

# Source Directory
source_dir_label = tk.Label(root, text="Source Directory:")
source_dir_label.grid(row=0, column=0, sticky="w")
source_dir_entry = tk.Entry(root, width=40)
source_dir_entry.grid(row=0, column=1)
source_dir_button = tk.Button(root, text="Browse", command=browse_source_dir)
source_dir_button.grid(row=0, column=2)

# Checkboxes and Destination Directories
delete_var = tk.BooleanVar()
delete_checkbox = tk.Checkbutton(root, text="Delete files after move", variable=delete_var)
delete_checkbox.grid(row=100, column=0, sticky="w")


row_num = 1
for file_type, data in FILE_TYPES.items():
    data["var"] = tk.BooleanVar()
    data["entry"] = tk.Entry(root, width=40)
    data["entry"].grid(row=row_num, column=1)
    checkbutton = tk.Checkbutton(root, text=data["label"], variable=data["var"])
    checkbutton.grid(row=row_num, column=0, sticky="w")
    browse_button = tk.Button(root, text="Browse", command=lambda ft=file_type: browse_dest_dir(ft))
    browse_button.grid(row=row_num, column=2)
    row_num += 1


# Process Button
process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.grid(row=row_num, column=1)

# Preset Buttons
update_preset_button = tk.Button(root, text="Save Preset", command=save_preset, state="disabled")
update_preset_button.grid(row=row_num + 1, column=0)
load_preset_button = tk.Button(root, text="Load Preset", command=load_preset)
load_preset_button.grid(row=row_num + 1, column=1)

if __name__ == "__main__":
    try:
        root.mainloop()
    except Exception as e:
        logger.exception(f"Unhandled exception occurred: {e}")
