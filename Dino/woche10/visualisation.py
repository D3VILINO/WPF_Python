from tkinter import *
from functions import solve

def open_window():
  window:Tk = Tk()
  window.geometry("300x300")
  window.resizable(False,False)

  root:Frame = Frame(window)
  root.pack()

  create_header(root)
  create_body(root)

  window.mainloop()

def create_header(root:Frame) -> None:
  header_frame:Frame = Frame(root)
  header_frame.pack(pady=20)

  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text="Lineares Gleichungssystem lösen", font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()


def create_body(root:Frame) -> None:
  body_frame:Frame = Frame(root)
  body_frame.pack()

  Label(body_frame, text="Geben Sie hier Ihre lineare Funktion ein: ").pack()

  entry:Entry = Entry(body_frame)
  entry.pack()

  solution:Label = Label()

  Button(body_frame, text="Lösen", command=lambda:solve(entry.get().replace(" ", ""), solution)).pack()
  Button(body_frame, text="Löschen", command=lambda: entry.delete(0, END)).pack()

  solution.pack()
