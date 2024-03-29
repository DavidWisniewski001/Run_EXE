import os
import csv
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def run_executable(executable_path):
    try:
        # Run the executable using subprocess.run()
        subprocess.run([executable_path], check=True)
        messagebox.showinfo("Success", f"Executable '{executable_path}' ran successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running executable '{executable_path}': {e}")

def run_executables_from_folder(folder_path):
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", f"'{folder_path}' is not a valid folder path.")
        return
    
    executables = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    
    for executable in executables:
        run_executable(executable)

def run_executables_from_csv(csv_path):
    try:
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    executable_path = row[0]
                    run_executable(executable_path)
    except FileNotFoundError:
        messagebox.showerror("Error", f"CSV file '{csv_path}' not found.")

def run_selected_option():
    selected_option = option_var.get()
    
    if selected_option == "Folder":
        folder_path = filedialog.askdirectory(title="Select Folder with Executables")
        if folder_path:
            run_executables_from_folder(folder_path)
    elif selected_option == "CSV":
        csv_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
        if csv_path:
            run_executables_from_csv(csv_path)

# Create the main window
window = tk.Tk()
window.title("Executable Runner")

# Create a label and dropdown for selecting the option
option_label = tk.Label(window, text="Select option:")
option_label.pack()

option_var = tk.StringVar(window)
option_var.set("Folder")  # Default option
option_dropdown = tk.OptionMenu(window, option_var, "Folder", "CSV")
option_dropdown.pack()

# Create a button to run the selected option
run_button = tk.Button(window, text="Run Selected Option", command=run_selected_option)
run_button.pack()

# Run the main event loop
window.mainloop()

