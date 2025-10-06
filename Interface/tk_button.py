from tkinter import *

window = Tk()

window.title('Botton')

btn_end = Button(window, text='Close', command=exit)

def tog():
    if window.cget('bg') == 'yellow':
        window.configure(bg = 'gray')
    else:
        window.configure( bg = 'yellow')

btn_log = Button(window, text='Switch', command=tog)


btn_log.pack(padx=150, pady=20)
btn_end.pack(padx=150, pady=20)

window.mainloop()