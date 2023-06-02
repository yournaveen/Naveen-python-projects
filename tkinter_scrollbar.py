#scroll bar widget is used to scroll the window to down or up or left or right inform of horizontal and vertical
from tkinter import *
window=Tk()
window.title("Scroll bar widget")
window.geometry("500x700")
vs=Scrollbar(window)
vs.pack(side=RIGHT,fill=Y)#side is used to side down to what side
                          #fill working with axis x and y 
l1=Listbox(window,yscrollcommand=vs.set,width=100,font=('bold'))
                 #yscrollcommand=setting the scroll bar in which axis
for i in range(50):
    l1.insert(END,'This is one of the most dangerous widget to learn to fullfill this go to youtube')
l1.pack(side=LEFT,fill=BOTH)
vs.config(command=Listbox.yview)
   #config has various attributes command is one of that connecting listbox and scroll bar

window.mainloop()
