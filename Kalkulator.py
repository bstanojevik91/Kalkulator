import tkinter as tk
from tkinter import ttk

# Step 2: Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Step 3: Create a variable to store the expression
expression = tk.StringVar()

# Step 4: Create the entry widget to display the expression
entry = ttk.Entry(root, textvariable=expression, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Step 5: Create a function to update the expression
def update_expression(value):
    if value == 'C':
        expression.set('')
    else:
        current_expression = expression.get()
        expression.set(current_expression + str(value))

# Step 6: Create buttons for numbers and operators, including 'C' for clear
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'  # Added 'C' button
]

row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(root, text=button, command=lambda btn=button: update_expression(btn)).grid(row=row_val, column=col_val, ipadx=20, ipady=20)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Step 7: Create a function to evaluate the expression
def calculate_expression():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("Error")

# Step 8: Create the equal button
ttk.Button(root, text='=', command=calculate_expression).grid(row=row_val, column=col_val, columnspan=2, ipadx=20, ipady=20)

# Step 9: Run the main loop
root.mainloop()
