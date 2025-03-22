import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Product: {result}")
    except ValueError:
        result_label.config(text="Invalid Input! Enter numbers only.")

root = tk.Tk()
root.title("Multiplication App")
root.geometry("300x200")

tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

calculate_btn = tk.Button(root, text="Multiply", command=calculate_product)
calculate_btn.pack(pady=10)

result_label = tk.Label(root, text="Product: ")
result_label.pack(pady=5)

root.mainloop()
        

