import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_and_run_bat(mode, file1, file2):
    if mode == 1:
        commands = [
            f'@echo off',
            f'call font.exe "{file1}" "{file2}"',
            'exit'
        ]
    elif mode == 2:
        commands = [
            f'@echo off',
            f'call font.exe "{file2}" "{file1}"',
            'exit'
        ]
    else:
        raise ValueError("ERROR")

    bat_file_path = 'temp_conversion.bat'
    with open(bat_file_path, 'w') as bat_file:
        bat_file.write('\n'.join(commands))

    try:
        subprocess.run(bat_file_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        messagebox.showinfo("Done", "The conversion is completed")
    except Exception as e:
        messagebox.showerror("ERROR", str(e))
    finally:
        os.remove(bat_file_path)

def run_conversion():
    mode = int(mode_var.get())
    file1 = file1_entry.get()
    file2 = file2_entry.get()
    
    if not file1.endswith('.oft.1'):
        messagebox.showwarning("Warning", "File 1 must have the extension .oft.1.")
        return
    if not file2.endswith('.ttf'):
        messagebox.showwarning("Warning", "File 2 must have the .ttf extension.")
        return
    
    generate_and_run_bat(mode, file1, file2)

def select_file1():
    file_path = filedialog.askopenfilename(filetypes=[("RE Engine Fonts", "*.oft.1")])
    file1_entry.delete(0, tk.END)
    file1_entry.insert(0, file_path)

def select_file2():
    file_path = filedialog.askopenfilename(filetypes=[("TrueType Fonts", "*.ttf")])
    file2_entry.delete(0, tk.END)
    file2_entry.insert(0, file_path)

def create_file1():
    file_path = filedialog.asksaveasfilename(defaultextension=".oft.1", filetypes=[("RE Engine Fonts", "*.oft.1")])
    if file_path:
        with open(file_path, 'w') as f:
            pass  
        file1_entry.delete(0, tk.END)
        file1_entry.insert(0, file_path)

def create_file2():
    file_path = filedialog.asksaveasfilename(defaultextension=".ttf", filetypes=[("TrueType Fonts", "*.ttf")])
    if file_path:
        with open(file_path, 'w') as f:
            pass  
        file2_entry.delete(0, tk.END)
        file2_entry.insert(0, file_path)


root = tk.Tk()
root.title("RE Engine fonts converter")


mode_var = tk.StringVar(value="1")
tk.Label(root, text="Select the conversion mode:").pack()
tk.Radiobutton(root, text="Convert *.oft.1 to *.ttf", variable=mode_var, value="1").pack()
tk.Radiobutton(root, text="Convert *.ttf to *.oft.1", variable=mode_var, value="2").pack()


tk.Label(root, text="Select file 1 (extension .oft.1):").pack()
file1_entry = tk.Entry(root, width=50)
file1_entry.pack()
frame1 = tk.Frame(root)
frame1.pack()
tk.Button(frame1, text="Select file", command=select_file1).pack(side=tk.LEFT)
tk.Button(frame1, text="Create file", command=create_file1).pack(side=tk.LEFT)

tk.Label(root, text="Select file 2 (extension .ttf):").pack()
file2_entry = tk.Entry(root, width=50)
file2_entry.pack()
frame2 = tk.Frame(root)
frame2.pack()
tk.Button(frame2, text="Select file", command=select_file2).pack(side=tk.LEFT)
tk.Button(frame2, text="Create file", command=create_file2).pack(side=tk.LEFT)


tk.Button(root, text="Start the conversion", command=run_conversion).pack()


root.mainloop()
