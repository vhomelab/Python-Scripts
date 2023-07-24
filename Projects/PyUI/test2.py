import tkinter as tk
from tkinter import *
from tkinter import ttk


# Functions
def btn_a_fn(a, b):
    lbl_a_var = a + b
    return lbl_a_var


window = tk.Tk()
window.title("Test2 app")
window.geometry("500x300")
# print(window.configure())

inf_a_var = tk.IntVar()
inf_b_var = tk.IntVar()
lbl_a_var = tk.IntVar()

lbl_a = ttk.Label(window, text="default", textvariable=lbl_a_var)
lbl_a.pack()

inf_a = ttk.Entry(window, textvariable=inf_a_var)
inf_b = ttk.Entry(window, textvariable=inf_b_var)
inf_a.pack()
inf_b.pack()

btn_a = ttk.Button(window, text='Click', command=btn_a_fn(inf_a_var, inf_b_var))
btn_a.pack()

window.mainloop()
