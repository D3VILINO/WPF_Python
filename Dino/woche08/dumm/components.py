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

def create_start(frame_body:Frame, header_label:Label) -> None:
  clear_frame(frame_body)

  entry:Entry = Entry(frame_body, text="New Database", font=("Helvetica", 16))
  entry.grid(row=0, column=0, columnspan=3, padx=5, pady=20)

  button:Button = Button(frame_body, text="New Database", padx=5, font=("Helvetica", 16), command=partial(get_database, frame_body, entry, header_label, "create"))
  button.grid(row=1, column=0, padx=5)
  button = Button(frame_body, text="Open Database", padx=5, font=("Helvetica", 16), command=partial(get_database, frame_body, entry, header_label, "open"))
  button.grid(row=1, column=1, padx=5)
  button = Button(frame_body, text="Exit", padx=5, font=("Helvetica", 16), command=exit)
  button.grid(row=1, column=2, padx=5)

def create_options(frame_body:Frame, header_label:Label) -> None:
  clear_frame(frame_body)

