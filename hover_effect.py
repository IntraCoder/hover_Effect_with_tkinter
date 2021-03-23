from tkinter import *

root = Tk()
root.geometry("300x300")

but = Button(root, text="Hover", font=(None, 17),
             bg="black", fg="white")
but.place(x=30, y=50)


def hover_effect(event):
    but.config(bg="wheat", fg="black")


def leave_effect(event):
    but.config(bg="black", fg="white")


but.bind("<Enter>", hover_effect)
but.bind("<Leave>", leave_effect)

root.mainloop()
