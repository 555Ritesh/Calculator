# CALCULATOR


import tkinter as tk
from tkinter import *
from tkinter import messagebox  

expression = ""
result_value = 0
operator = ""

def button_clicked(number):
    global expression
    expression = expression + str(number)
    update_display()

def operator_clicked(operator_sign):
    global result_value, expression, operator
    result_value = float(expression)
    operator = operator_sign
    expression = expression + operator
    update_display()

def equal_clicked():
    global result_value, expression
    try:
        if operator == "+":
            result_value += float(expression.split("+")[1])
        elif operator == "-":
            result_value -= float(expression.split("-")[1])
        elif operator == "*":
            result_value *= float(expression.split("*")[1])
        elif operator == "/":
            denominator = float(expression.split("/")[1])
            if denominator != 0:
                result_value /= denominator
            else:
                messagebox.showerror("Error", "Division by zero not allowed.")
                reset_calculator()
                return

        expression = str(result_value)
        update_display()
    except:
        messagebox.showerror("Error", "Invalid expression")

def clear_clicked():
    global result_value, expression, operator
    reset_calculator()

def update_display():
    data_var.set(expression)

def reset_calculator():
    global result_value, expression, operator
    expression = ""
    result_value = 0
    operator = ""
    update_display()

gui_window = tk.Tk()
gui_window.geometry("320x400+400+400")
gui_window.resizable(0, 0)
gui_window.title("Calculator")

data_var = StringVar()
data_label = Label(
    gui_window,
    text="Label",
    anchor=SE,
    font=("Cambria Math", 20),
    textvariable=data_var,
    background="#ffffff",
    fg="#000000"
)
data_label.pack(expand=True, fill="both")

buttons_frame = Frame(gui_window, bg="#000000")
buttons_frame.pack(expand=True, fill="both")

buttons_layout = [
    "123C",
    "456+",
    "789-",
    "0/*="
]

for row in buttons_layout:
    row_frame = Frame(buttons_frame, bg="#000000")
    row_frame.pack(expand=True, fill="both")

    for char in row:
        button_text = char
        if char.isdigit():
            button = Button(
                row_frame,
                text=button_text,
                font=("Cambria", 22),
                relief=GROOVE,
                border=0,
                command=lambda b=button_text: button_clicked(b)
            )
        elif char in "+-*/":
            button = Button(
                row_frame,
                text=button_text,
                font=("Cambria", 22),
                relief=GROOVE,
                border=0,
                command=lambda op=button_text: operator_clicked(op)
            )
        elif char == "=":
            button = Button(
                row_frame,
                text=button_text,
                font=("Cambria", 22),
                relief=GROOVE,
                border=0,
                command=equal_clicked
            )
        elif char == "C":
            button = Button(
                row_frame,
                text=button_text,
                font=("Cambria", 22),
                relief=GROOVE,
                border=0,
                command=clear_clicked
            )
        button.pack(side=LEFT, expand=True, fill="both")

gui_window.mainloop()
