import tkinter as tk
from tkinter import messagebox

# ------------------ OOP DESIGN ------------------ #
class Zenith:
    def __init__(self, name):
        self.name = name

    def mutual_services(self):
        return [
            "Lines of credit",
            "Investment management and accounts",
            "Insurance"
        ]

    def unique_services(self):
        return []

class RetailBanking(Zenith):
    def unique_services(self):
        return [
            "Retirement and education accounts",
            "Loans and mortgages",
            "Checking and saving"
        ] + self.mutual_services()

class GlobalBanking(Zenith):
    def unique_services(self):
        return [
            "Multi-currency management services and products",
            "Foreign currency accounts",
            "Foreign currency credit cards",
            "Transborder advisory services",
            "Liquidity management"
        ]

class CommercialBanking(Zenith):
    def unique_services(self):
        return [
            "Advisory services"
        ] + self.mutual_services()

# ------------------ GUI DESIGN ------------------ #
def show_services():
    name = name_entry.get().strip()
    division = division_var.get()

    if not name or division == "Select Division":
        messagebox.showerror("Error", "Please enter a name and select a division.")
        return

    if division == "Retail Banking":
        emp = RetailBanking(name)
    elif division == "Global Banking":
        emp = GlobalBanking(name)
    elif division == "Commercial Banking":
        emp = CommercialBanking(name)
    else:
        messagebox.showerror("Error", "Invalid division selected.")
        return

    services = emp.unique_services()
    result_text.set(f"{name} works in {division} and offers these services:\n\n- " + "\n- ".join(services))


# ------------------ MAIN WINDOW ------------------ #
root = tk.Tk()
root.title("Zenith Bank Employee Services")
root.geometry("500x400")
root.resizable(False, False)

# Input Fields
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Employee Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, width=40)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Select Division:").grid(row=1, column=0, sticky="w")
division_var = tk.StringVar(value="Select Division")
divisions = ["Retail Banking", "Global Banking", "Commercial Banking"]
tk.OptionMenu(frame, division_var, *divisions).grid(row=1, column=1, sticky="w")

tk.Button(frame, text="Show Services", command=show_services).grid(row=2, column=1, pady=10, sticky="e")

# Output
result_text = tk.StringVar()
output_label = tk.Label(root, textvariable=result_text, wraplength=450, justify="left", padx=20)
output_label.pack()

root.mainloop()
