from tkinter import *
window=Tk()
window.geometry("700x500")
window.title("GRID Layout")
l1=Button(window,text="row0column0",bg='blue')
l1.grid(row=0,column=0)#Grid Capital G should be there
l2=Button(window,text="row0column1",bg='red')
l2.grid(row=0,column=1)
l3=Button(window,text="row1column1",bg='purple')
l3.grid(row=1,column=1)
#giving space usong padx in grid
l4=Button(window,text="row2column2",bg='yellow')
l4.grid(row=2,column=3,padx=10)
l5=Button(window,text="row2column3",bg='pink')
l5.grid(row=2,column=3,padx=20)
#using rowspan merging two cells into one cell
l6=Button(window,text="row4column4",bg='orange')
l6.grid(row=4,column=4,rowspan=2)
l7=Button(window,text="row4column5",bg='orange')
l7.grid(row=4,column=5)
l8=Button(window,text="row4column6",bg='orange')
l8.grid(row=4,column=6)
mainloop()
