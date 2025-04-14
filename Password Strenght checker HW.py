from tkinter import *

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result.config(text="Please enter a password", fg="orange")
    elif length < 5:
        result.config(text="Weak Password", fg="red")
    elif 5 <= length < 8:
        result.config(text="Moderate Password", fg="blue")
    else:
        result.config(text="Strong Password", fg="green")

# Create window
window = Tk()
window.title("Password Strength Checker")
window.geometry("300x150")

# Widgets
Label(window, text="Enter Password:").pack(pady=5)
entry = Entry(window, show="*")
entry.pack(pady=5)

Button(window, text="Check Strength", command=check_strength).pack(pady=5)
result = Label(window, text="")
result.pack(pady=5)

window.mainloop()
