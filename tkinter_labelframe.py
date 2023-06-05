from tkinter import *
window=Tk()
window.title("Label frame")
window.geometry("500x400")
f=LabelFrame(window,width=200,height=300,bg='#00ff88',text="inside the text frame")
f.pack()
window.mainloop()
