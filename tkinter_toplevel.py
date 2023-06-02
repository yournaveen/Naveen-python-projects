from tkinter import *
window=Tk()
window.title("Top level window")
window.geometry("500x400")
def secondwindow():
    tp=Toplevel()
#top level widget creates a new window
    tp.title("second window")
    tp.geometry("400x300")
    l=Label(tp,text='This is second window').pack()
    b2=Button(tp,text="click to close the second window",command=tp.destroy).pack()
    
b1=Button(window,text="click to view second window",command=secondwindow).pack()
window.mainloop()

