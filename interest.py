import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Get inputs
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Calculate Simple Interest
        simple_interest = (principal * rate * time) / 100

        # Calculate Compound Interest
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        # Display results
        label_si_result.config(text=f"Simple Interest: {simple_interest:.2f}")
        label_ci_result.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")
root.resizable(False, False)

# UI Layout
tk.Label(root, text="Principal (₹):").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()
tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time (years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

tk.Button(root, text="Calculate Interest", command=calculate_interest).pack(pady=15)

label_si_result = tk.Label(root, text="Simple Interest: ₹0.00")
label_si_result.pack(pady=5)

label_ci_result = tk.Label(root, text="Compound Interest: ₹0.00")
label_ci_result.pack(pady=5)

# Start the GUI event loop
root.mainloop()

