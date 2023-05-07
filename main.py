import tkinter as tk

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Define a function to perform the selected operation
def perform_operation():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = subtract(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        if num2 == 0:
            result = 'Cannot divide by zero'
        else:
            result = divide(num1, num2)

    result_label.config(text=result)

# Create the GUI window
root = tk.Tk()
root.title('Calculator')

# Create the input fields and labels
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0)

operation_var = tk.StringVar(value='Add')
operation_menu = tk.OptionMenu(root, operation_var, 'Add', 'Subtract', 'Multiply', 'Divide')
operation_menu.grid(row=0, column=1)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2)

# Create the button to perform the operation
button = tk.Button(root, text='Calculate', command=perform_operation)
button.grid(row=1, column=1)

# Create the label to display the result
result_label = tk.Label(root, text='')
result_label.grid(row=2, column=1)

# Start the GUI event loop
root.mainloop()
