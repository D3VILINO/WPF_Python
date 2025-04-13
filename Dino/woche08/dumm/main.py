from tkinter import *
from components import *
from functions import create_database_folder
from passwordmanager import main as passwordmanager_main

create_database_folder()

window:Tk = Tk()
window.geometry("800x600")

root:Frame = Frame(window)
root.pack()

header_label = create_header(root)
frame_body:Frame = Frame(root)
frame_body.pack()
create_start(root, header_label)

# passwordmanager_main()
window.mainloop()