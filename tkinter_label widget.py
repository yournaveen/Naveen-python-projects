from tkinter import *
#tkinter is a gui in python
#here we can see various types of widgets used by using tkinter
window=Tk()
window.title("Label widget")
window.geometry("500x200")
#window.resizable(height=False,width=False) this will disable to options to expand
window.configure()#set background color by giving color name


#Label widget is a textable widget were you can enter your textable wordings
#you can give various number of Label attributes within the Label parameter like
#changing the color of font use fg="color name"
#changing the color of background font use bg="color name"
#changing the size of font use font="text format name",by size use size=value
l1=Label(window,text="This is label widget:",fg="black")
l1.pack()#layout manager places the widget by giving attributes of the grid()
l2=Label(window,text="Enter your name:",fg="#00ff93",justify="left")
#here justify option is used to justify the position by giving values like left,right,top,bottom
l2.pack()
window.mainloop()

