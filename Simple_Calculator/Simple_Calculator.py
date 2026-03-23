from tkinter import *

def click(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# window
root = Tk()
root.title("Simple Calculator")
root.geometry("300x350")

# display box
entry = Entry(root, font=("Arial", 20), bd=5, relief=RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# buttons
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 1
col = 0

for b in buttons:
    if b == "=":
        Button(root, text=b, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        Button(root, text=b, width=5, height=2,
               command=lambda x=b: click(x)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# clear button
Button(root, text="Clear", width=22, command=clear).grid(row=row, column=0, columnspan=4)

root.mainloop()
