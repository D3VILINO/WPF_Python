from tkinter import Button, Entry, Frame

def create_display(master:Frame) -> None:
  label_display = Entry(master, state="disabled", width=30)
  label_display.pack()

def create_left_collumn(master:Frame) -> None:
  label_what = Entry(master, state="disabled", font=("Helvetica", 16), width=2, border=1, borderwidth=1)
  label_what.pack(pady="1")

  button_MC = Button(text="MC")
  button_MC.pack(pady="1")

  button_MR = Button(text="MR")
  button_MR.pack(pady="1")

  button_MS = Button(text="MS")
  button_MS.pack(pady="1")

  button_M_add = Button(text="M+")
  button_M_add.pack(pady="1")