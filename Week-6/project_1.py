import tkinter as tk
from tkinter import messagebox as msgbox

def calculate_charge():
    location = location_entry.get().lower()
    weight_text = float(weight_entry.get())

    #shows error if nothing is inputed
    if weight_text == "":
        msgbox.showerror("Error", "Please enter the package weight.")
        return
    
    #conditions for different locations
    if location == "ibeju-lekki":
        weight = float(weight_text)
        if weight >= 10:
            amount = 5000
        else:
            amount = 3500
        msgbox.showinfo("Delivery Charge", "The delivery charge is ₦" + str(amount))

    elif location == "epe":
        weight = float(weight_text)
        if weight >= 10:
            amount = 10000
        else:
            amount = 5000
        msgbox.showinfo("Delivery Charge", "The delivery charge is N" + str(amount))
    #Making sure that it's either of the 2 locations
    else:
        msgbox.showerror("Error", "We only deliver to Ibeju-Lekki or Epe.")

# Main window
root = tk.Tk()
root.title("Simi Services - Delivery Checker")
root.geometry("960x540")

# Location input
location_label = tk.Label(root, text="Enter Delivery Location (Ibeju-Lekki or Epe):")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack(pady =10) 

# Weight input
weight_label = tk.Label(root, text="Enter Package Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root, width= 6)
weight_entry.pack(pady = 10)

# Submit button
submit_button = tk.Button(root, text="Check Price", command=calculate_charge)
submit_button.pack(pady =10)

#Styling the button widget
submit_button.config(fg = "white", bg = "green", activebackground= "white", activeforeground= "green", height= 3, width= 20)

# Start GUI
root.mainloop()
