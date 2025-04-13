from tkinter import *
from functions import *


# ich habe den Bezahlvorgang vergessen zu implementieren, aber leider keine Zeit mehr dies vor Abgabeende hinzuzufügen
window:Tk = Tk()
window.geometry("800x600")

root:Frame = Frame(window)
root.pack()

create_header(root)
frame_body:Frame = Frame(root)
frame_body.pack()
create_power(frame_body)

window.mainloop()