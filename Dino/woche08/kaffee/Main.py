from tkinter import *
from functions import *

window:Tk = Tk()
window.geometry("800x600")

root:Frame = Frame(window)
root.pack()

create_header(root)
frame_body:Frame = Frame(root)
frame_body.pack()
create_power(frame_body)

window.mainloop()