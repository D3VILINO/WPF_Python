from tkinter import *
from components import *
from passwordmanager import main as passwordmanager_main

window:Tk = Tk()
window.geometry("800x600")

root:Frame = Frame(window)
root.pack()

header_label = create_header(root)
create_body(root, header_label)

# passwordmanager_main()
window.mainloop()