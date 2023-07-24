import tkinter as tk
from tkinter import *
from tkinter import ttk
def changeLabel():
    # ttkField_1['state'] = 'disabled'
    # tkLabel_1['text'] = ttkField_1.get()
    tkText_1['state'] = 'normal'

    tkText_1.insert('end', ttkField_1.get())
    tkText_1['state'] = 'disabled'


window = tk.Tk()
window.geometry('600x250')
window.title("MyAppl")

tkLabel_1 = tk.Label(master=window, text="First Label")
tkLabel_1.pack()
ttkField_1 = ttk.Entry(master=window)
ttkField_1.pack()
tkBtn_1 = tk.Button(master=window, text="Click It!", command=changeLabel)
tkBtn_1.pack()
tkText_1 = tk.Text(
    master=window,
    width=100, height=30,
    wrap=WORD,
    padx=5, pady=5,
    state='normal'
    # yscrollcommand=True
)
tkText_1.pack()

window.mainloop()