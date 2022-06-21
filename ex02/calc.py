import tkinter as tk
from tkinter import messagebox as tkm

calc = tk.Tk()
calc.geometry("300x500")
calc.title("電卓")

entry = tk.Entry(justify = "right", width =11, font = ("Times New Roman", 40))
entry.grid(row = 0, columnspan = 3)

fonts = ("Times New Roman", 20)

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)

def equal(event):
    siki = entry.get()
    entry.delete(0, tk.END)
    kotae = eval(siki)
    entry.insert(tk.END, kotae)

x = 0
list = [[7,0],
        [6,2],[6,1],[6,0],
        [5,2],[5,1],[5,0],[4,2],[4,1],[4,0]]
for i in list:
    button = tk.Button(text = x, font = fonts, width = 6, height = 2, foreground = 'black')
    button.bind("<1>", button_click)
    button.grid(row = i[0], column = i[1], padx = 0, pady = 0)
    x += 1

buttonequal = tk.Button(text = "=", font = fonts, width = 4, height = 1, background = "sky blue")
buttonequal.bind("<1>", equal)
buttonequal.grid(row = 7, column = 2, padx = 0, pady = 0)

list1 = [["+"]]
y = 3
for i in list1:
    button = tk.Button(text = i, font = fonts, width = 4, height = 1, background = "gray")
    button.bind("<1>", button_click)
    button.grid(row = y, column = 2, padx = 0, pady = 0)

calc.mainloop()