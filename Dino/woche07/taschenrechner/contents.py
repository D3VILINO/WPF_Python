from tkinter import Button, Entry, Frame

def create_display(master:Frame) -> None:
  label_display = Entry(master, state="disabled", width=30)
  label_display.pack()

def create_left_collumn(master:Frame) -> None:
  label_what = Entry(master, state="disabled", font=("Helvetica", 16), width=2, border=1, borderwidth=1)
  label_what.pack(pady="1")

  button_MC = Button(master, text="MC")
  button_MC.pack(pady="1")

  button_MR = Button(master, text="MR")
  button_MR.pack(pady="1")

  button_MS = Button(master, text="MS")
  button_MS.pack(pady="1")

  button_M_add = Button(master, text="M+")
  button_M_add.pack(pady="1")

def create_body(master:Frame) -> None:
  button_backspace = Button(text="Backspace")
  button_backspace.grid(row=0, column=0, columnspan=5, padx=1, pady=1)

  button_CE = Button(text="CE")
  button_CE.grid(row=0, column=5, columnspan=5, padx=1, pady=1)

  button_C = Button(text="C")
  button_C.grid(row=0, column=10, columnspan=5, padx=1, pady=1)