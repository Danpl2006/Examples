from tkinter import *
import tkinter.messagebox as box

window = Tk()

window.title('butt')

def dialog():
    var = box.askyesno('Mass box', 'Proceed?')
    if var == 1:
        box.showinfo('Yes Box', 'Proceeding...')
    else:
        box.showwarning('NO BOX', 'Cancelling...')

btn = Button(window, text='Click', command=dialog)

btn.pack(padx=150, pady=50)

window.mainloop()