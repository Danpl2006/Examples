from tkinter import *
import tkinter.messagebox as box

window = Tk()

window.title('list')

frame = Frame(window)

listbox =  Listbox(frame)
listbox.insert(1, 'HTML')
listbox.insert(2, 'CSS')
listbox.insert(3, 'JS')

def dialog():
    box.showinfo('Selection', 'Ur choice:' + \
    listbox.get(listbox.curselection()))

btn = Button(frame, text='Choose', command=dialog)

btn.pack(side=RIGHT, padx=5)
listbox.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()
