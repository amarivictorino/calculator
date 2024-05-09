import tkinter as tk
from tkinter import messagebox

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero!"

def calculate():
    choice = operation_var.get()
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())

    if choice == 1:
        result_label.config(text="Result: " + str(addition(num1, num2)))
    elif choice == 2:
        result_label.config(text="Result: " + str(subtraction(num1, num2)))
    elif choice == 3:
        result_label.config(text="Result: " + str(multiplication(num1, num2)))
    elif choice == 4:
        result_label.config(text="Result: " + str(division(num1, num2)))

def clear_entries():
    num1_entry.delete(0, 'end')
    num2_entry.delete(0, 'end')
    result_label.config(text="Result:")

def exit_program():
    messagebox.showinfo("Message", "Thank you!")
    window.destroy()

window = tk.Tk()
window.title("Simple Calculator")

operation_var = tk.IntVar()
num1_label = tk.Label(window, text="Enter first number:")
num1_label.grid(row=0, column=0, padx=10, pady=5)
num1_entry = tk.Entry(window)
num1_entry.grid(row=0, column=1, padx=10, pady=5)

operation_label = tk.Label(window, text="Choose operation:")
operation_label.grid(row=1, column=0, padx=10, pady=5)
addition_radio = tk.Radiobutton(window, text="Addition", variable=operation_var, value=1)
addition_radio.grid(row=1, column=1, padx=10, pady=5)
subtraction_radio = tk.Radiobutton(window, text="Subtraction", variable=operation_var, value=2)
subtraction_radio.grid(row=2, column=1, padx=10, pady=5)
multiplication_radio = tk.Radiobutton(window, text="Multiplication", variable=operation_var, value=3)
multiplication_radio.grid(row=3, column=1, padx=10, pady=5)
division_radio = tk.Radiobutton(window, text="Division", variable=operation_var, value=4)
division_radio.grid(row=4, column=1, padx=10, pady=5)

num2_label = tk.Label(window, text="Enter second number:")
num2_label.grid(row=5, column=0, padx=10, pady=5)
num2_entry = tk.Entry(window)
num2_entry.grid(row=5, column=1, padx=10, pady=5)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(window, text="Result:")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

clear_button = tk.Button(window, text="Clear", command=clear_entries)
clear_button.grid(row=8, column=0, padx=10, pady=5)

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.grid(row=8, column=1, padx=10, pady=5)

window.mainloop()



    



