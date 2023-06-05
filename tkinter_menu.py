from tkinter import *
window=Tk()
window.title("MENU BARS")
window.geometry("600x700")
def exit():
    menubar.quit
    
menubar=Menu(window)
submenu=Menu(menubar,tearoff=0)
subedit=Menu(menubar,tearoff=0)
submenu.add_command(label="New file")
submenu.add_command(label="open")
submenu.add_command(label="save")
submenu.add_command(label="save As...")
submenu.add_command(label="exit",command=quit)
menubar.add_cascade(label="File",menu=submenu)
subedit.add_command(label="undo")
subedit.add_command(label="redo")
menubar.add_cascade(label="Edit",menu=subedit)
window.config(menu=menubar)
window.mainloop()
