from tkinter import *
import tkinter.messagebox as box

window = Tk()

window.title('check btn')

frame = Frame(window)

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()

book_1 = Checkbutton(frame, text='Html', variable=var_1, onvalue=1, offvalue= 0)
book_2 = Checkbutton(frame, text='Css', variable=var_2, onvalue=1, offvalue= 0)
book_3 = Checkbutton(frame, text='js', variable=var_3, onvalue=1, offvalue= 0)

def dialog():
    str = 'Ur choice'
    if var_1.get() == 1: str += '\nHtml easy'
    if var_2.get() == 1: str += '\ncss easy'
    if var_3.get() == 1: str += '\njs easy'
    box.showinfo('Select', str)

btn = Button(frame, text='Choose', command=dialog)

btn.pack(side=RIGHT, padx=5)
book_1.pack(side=LEFT)
book_2.pack(side=LEFT)
book_3.pack(side=LEFT)

frame.pack(padx=30, pady=30)

window.mainloop()