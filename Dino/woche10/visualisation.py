from tkinter import *
from functions import solve, test_import

def open_window():
  window:Tk = Tk() #type:ignore[annotation-unchecked]
  window.geometry("300x300")
  window.resizable(False,False)

  root:Frame = Frame(window) #type:ignore[annotation-unchecked]
  root.pack()

  create_header(root)
  create_body(root)

  window.mainloop()


def create_header(root:Frame) -> None:
  header_frame:Frame = Frame(root)
  header_frame.pack(pady=20)

  Label(header_frame, text="="*30, font=("Courier New", 12)).pack()
  Label(header_frame, text="Lineares Gleichungssystem lösen", font=("Courier New", 12)).pack()
  Label(header_frame, text="="*30, font=("Courier New", 12)).pack()

def test(root):
  window = Toplevel(root) #type:ignore[annotation-unchecked]
  window.geometry("300x300")
  window.resizable(False,False)

  root:Frame = Frame(window) #type:ignore[annotation-unchecked]
  root.pack()

  window.mainloop()


def create_body(root:Frame) -> None:
  body_frame:Frame = Frame(root)
  button_frame:Frame = Frame(body_frame)

  info_label = Label(body_frame, text="Geben Sie hier Ihre lineare Funktion ein: ")
  solution:Label = Label(body_frame, font=("Courier New", 12))

  entry:Entry = Entry(body_frame)
  entry.bind("<Return>", lambda e: solve_button.invoke())

  solve_button:Button = Button(button_frame, text="Lösen", command=lambda:solve(entry.get().replace(" ", ""), solution), width=8)
  delete_button:Button = Button(button_frame, text="Löschen", command=lambda: entry.delete(0, END), width=8)
  test_button:Button = Button(button_frame, text="insert", command=lambda: test_import(entry))

  test_test_button:Button = Button(button_frame, text="test test", command=lambda: test(root))

  body_frame.pack()
  info_label.pack()
  entry.pack()
  button_frame.pack(pady=8)
  solve_button.grid(row=0, column=0, padx=4)
  delete_button.grid(row=0, column=1, padx=4)
  test_button.grid(row=0, column=2)
  test_test_button.grid(row=0, column=3)
  solution.pack()
