from tkinter import *
window=Tk()
window.geometry("800x600")
window.title("listbox Food delicery")
listbox1=Listbox(window,width=50,height=5,bg='#006659')
#listbox is a selection of single or multiple lines of data
#selectmode="multiple"select mode performs multiple selection of the listed item we can give values as single and multiple according to the selection
#to insert or feed data into the list box we can use insert option
listbox1.insert(0,"Biriyani")
listbox1.insert(1,"kuska")
listbox1.insert(2,"curd")
listbox1.insert(3,"tikka")
listbox1.pack()
def order():
    a=listbox1.get(listbox1.curselection())#curselection is a predefined function that fetches the value(s) of a selected item or items.
    l2=Label(window,text="you have ordered\n"+a)
    l2.pack()
b1=Button(window,text="place your order",command=order)
b1.pack(pady=10)
window.mainloop()

