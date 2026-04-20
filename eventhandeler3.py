from tkinter import *
import tkinter as tk

mindow = tk.Tk()
mindow.geometry("400x400")
mindow.title("age calculator")

TITLE_labelXYZ = tk.Label(master=mindow, text="your birth year is:")
TITLE_labelXYZ.pack()

entyint = tk.IntVar()

enter = tk.Entry(master=mindow, textvariable=entyint)
enter.pack()

# Label with empty text initially
answer = tk.Label(master=mindow, text="")
answer.pack()

def age():
    x = entyint.get()
    result = 2026 - x
    answer.config(text=f"Your age is: {result}")  # update label when clicked

button = tk.Button(master=mindow, text="calculate age", command=age)
button.pack()

mindow.mainloop()


