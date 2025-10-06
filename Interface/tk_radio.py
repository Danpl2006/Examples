from tkinter import *
import tkinter.messagebox as box

window = Tk()

window.title('radio btn')

frame = Frame(window)

book = StringVar()

radio_1 = Radiobutton(frame, text='HTML',
                      variable=book, value='Html in easy')
radio_2 = Radiobutton(frame, text='CSS',
                      variable=book, value='CSS in easy')
radio_3 = Radiobutton(frame, text='JS',
                      variable=book, value='JS in easy')

radio_1.select()

def dialog():
    box.showinfo('SELECTION', 'Ur choice: \n' + book.get())

btn = Button(frame, text='Choose', command=dialog)
btn.pack(side=RIGHT, padx=5)
radio_1.pack(side=LEFT)
radio_2.pack(side=LEFT)
radio_3.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()