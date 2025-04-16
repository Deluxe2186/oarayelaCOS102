import tkinter as tk
from tkinter import messagebox as msgbox

def admission():
    name = name_entry.get().title()
    jamb = int(jamb_entry.get())
    credit = int(credit_entry.get())
    interview = int_entry.get()

    if name == "":
        msgbox.showerror("Error", "Please enter name.")
        return
    
    #for admitted students
    if jamb >= 250 and credit >= 5:
        name = name_entry
        jamb = jamb_entry
        credit = credit_entry
        admitted.append(name_entry)
    else:
        not_admitted.append(name_entry)

admitted =[]
not_admitted = []

# Main window
root = tk.Tk()
root.title("Simi Services - Delivery Checker")
root.geometry("960x540")

# Name input
name_entry = tk.Label(root, text="Enter name:")
name_entry.pack()
name_entry = tk.Entry(root)
name_entry.pack(pady =10) 

# Jamb input
jamb_entry = tk.Label(root, text="Enter jamb score:")
jamb_entry.pack()
jamb_entry = tk.Entry(root)
jamb_entry.pack(pady =10) 

# Credit input
credit_entry = tk.Label(root, text="Enter credits:")
credit_entry.pack()
credit_entry = tk.Entry(root)
credit_entry.pack(pady =10) 

# interview input
int_entry = tk.Label(root, text="Enter credits:")
int_entry.pack()
int_entry = tk.Radiobutton(root)
credit_entry.pack(pady =10) 

# Submit button
submit_button = tk.Button(root, text="Submit", command=admission)
submit_button.pack(pady =10)

# Start GUI
root.mainloop()