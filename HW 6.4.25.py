import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry_inch.get())  
        centimeters = inches * 2.54       
        result_label.config(text=f"{inches} inches is {centimeters} cm.") 
    except ValueError:
        result_label.config(text="Please enter a valid number.")  


root = tk.Tk()
root.title("Inches to Centimeters Converter")


input_label = tk.Label(root, text="Enter length in inches:")
input_label.pack()


entry_inch = tk.Entry(root)
entry_inch.pack()


convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()