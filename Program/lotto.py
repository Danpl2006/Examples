from tkinter import *
from random import sample

window = Tk()

img = PhotoImage(file='mem.gif')

img_lb1 = Label(window, image=img)

label_11 = Label(window, relief='groove', width=2)
label_12 = Label(window, relief='groove', width=2)
label_13 = Label(window, relief='groove', width=2)
label_14 = Label(window, relief='groove', width=2)
label_15 = Label(window, relief='groove', width=2)
label_16 = Label(window, relief='groove', width=2)

getBtn = Button(window)
resBtn = Button(window)

img_lb1.grid(row=1, column=1, rowspan=2)
label_11.grid(row=1, column=2, padx=10)
label_12.grid(row=1, column=3, padx=10)
label_13.grid(row=1, column=4, padx=10)
label_14.grid(row=1, column=2, padx=10)
label_15.grid(row=1, column=6, padx=10)
label_16.grid(row=1, column=7, padx=(10, 20))

getBtn.grid(row=2, column=2, columnspan=4)
resBtn.grid(row=2, column=6, columnspan=2)


window.title('Lotto number picker')
window.resizable(0, 0)
getBtn.configure(text='Get my lucky number')
resBtn.configure(text='Reset')

label_11.configure(text='...')
label_12.configure(text='...')
label_13.configure(text='...')
label_14.configure(text='...')
label_15.configure(text='...')
label_16.configure(text='...')

resBtn.configure(state=DISABLED)


def pick():
    nums = sample(range(1, 49), 6)
    label_11.configure(text=nums[0])
    label_12.configure(text=nums[1])
    label_13.configure(text=nums[2])
    label_14.configure(text=nums[3])
    label_15.configure(text=nums[4])
    label_16.configure(text=nums[5])
    getBtn.configure(state=DISABLED)
    resBtn.configure(state=NORMAL)

def reset():
    label_11.configure(text='...')
    label_12.configure(text='...')
    label_13.configure(text='...')
    label_14.configure(text='...')
    label_15.configure(text='...')
    label_16.configure(text='...')
    getBtn.configure(state=NORMAL)
    resBtn.configure(state=DISABLED)

getBtn.configure(command=pick)
resBtn.configure(command=reset)







window.mainloop()
