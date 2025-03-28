import os
from tkinter import Frame, PhotoImage, Tk
from contents import create_calculator

window = Tk()
window.title("Calculator")
window.iconphoto(False, PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")))
window.resizable(False, False)
window.geometry("315x250")

root = Frame(window)
root.pack(anchor="center", fill="both", pady="10", padx="25")

create_calculator(root)

window.mainloop()