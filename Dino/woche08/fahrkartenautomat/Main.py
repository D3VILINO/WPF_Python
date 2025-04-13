from tkinter import *
from functions import *

window:Tk = Tk()
window.geometry("350x350")
window.resizable(False,False)

root:Frame = Frame(window)
root.pack()

create_header(root)
body = Frame(root)
body.pack()
create_start(body)

window.mainloop()