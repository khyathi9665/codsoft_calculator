import tkinter as tk

def but_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)
def calcu():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
root = tk.Tk()
root.title("Simple Calculator")
entry = tk.Entry(root, width=20, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: but_click(b) if b != '=' else calcu()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=row, column=col)
root.mainloop()
