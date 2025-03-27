import os
from tkinter import Button, Frame, PhotoImage, Tk
import contents

window = Tk()
window.title("Calculator")
window.iconphoto(False, PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")))
window.resizable(False, False)
window.geometry("200x200")

root = Frame(window)
root.pack(anchor="center", fill="both", pady="10", padx="10")

contents.create_display(root)
contents.create_left_collumn(root)
contents.create_body(root)

window.mainloop()