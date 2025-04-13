from functools import partial
from tkinter import *
from functions import *

def create_header(frame:Frame) -> Label:
  frame_header:Frame = Frame(frame)
  frame_header.pack()

  header:Label = Label(frame_header, padx=5, text="="*41, font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)

  header = Label(frame_header, padx=5, text="Passwordmanager", font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)
  header_label = header

  header = Label(frame_header, padx=5, text="="*41, font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)
  return header_label

create_database_folder()

window:Tk = Tk()
window.geometry("800x600")

root:Frame = Frame(window)
root.pack()

header_label = create_header(root)
frame_body:Frame = Frame(root)
frame_body.pack()
create_start(frame_body, header_label)

window.mainloop()
