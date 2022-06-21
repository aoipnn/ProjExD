import tkinter as tk

calc = tk.Tk()
calc.geometry("300x450")
calc.title("すごい電卓")

entry = tk.Entry(justify = "right", width =11, font = ("Times New Roman", 40))
entry.grid(row = 0, columnspan = 10)

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

def delete(event):
    entry.delete(0, tk.END)


def delete_1(event):
    pos_end_prew = len(entry.get())-1
    entry.delete(pos_end_prew,tk.END)

def monkey(event):
    n = entry.get()
    m = int(n) * 2
    entry.delete(0, tk.END)
    entry.insert(tk.END, m)

def gorilla(event):
    o = entry.get()
    p = int(o) + 10
    entry.delete(0, tk.END)
    entry.insert(tk.END, p)

x = 0
list = [[6,1],[5,2],[5,1],[5,0],[4,2],[4,1],[4,0],[3,2],[3,1],[3,0]]
for i in list:
    button = tk.Button(text = x, font = fonts, width = 4, height = 1, foreground = 'black')
    button.bind("<1>", button_click)
    button.grid(row = i[0], column = i[1], padx = 2, pady = 4)
    x += 1

buttonequal = tk.Button(text = "=", font = fonts, width = 4, height = 1, background = "sky blue")
buttonequal.bind("<1>", equal)
buttonequal.grid(row = 7, column = 4, padx = 2, pady = 4)

buttonDel = tk.Button(text='C',font=fonts,width = 4, height = 1,background = "white",foreground = 'gray')
buttonDel.bind("<1>", delete)
buttonDel.grid(row = 2,column = 4,padx=2,pady = 4)

buttonAllDel = tk.Button(text = "D", font = fonts, width = 4, height = 1, background = "white", foreground = "gray")
buttonAllDel.bind("<1>", delete_1)
buttonAllDel.grid(row = 2, column = 2, padx = 2, pady = 4)

buttonMonkey = tk.Button(text="猿", font=fonts, width = 4, height = 1, background = "gray", foreground = "brown")
buttonMonkey.bind("<1>", monkey)
buttonMonkey.grid(row = 2, column = 0, padx = 2, pady = 4)

buttonGorilla = tk.Button(text="ゴリラ", font=fonts, width = 4, height = 1, background = "white", foreground = "black")
buttonGorilla.bind("<1>", gorilla)
buttonGorilla.grid(row = 2, column = 1, padx = 2, pady = 4)

list1 = [["+"], ["-"], ["*"], ["/"]]
y = 3
for i in list1:
    button = tk.Button(text = i, font = fonts, width = 4, height = 1, background = "gray")
    button.bind("<1>", button_click)
    button.grid(row = y, column = 4, padx = 2, pady = 4)
    y += 1

calc.mainloop()