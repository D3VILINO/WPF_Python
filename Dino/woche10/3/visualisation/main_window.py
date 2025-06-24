from visualisation.header import create_header
import globals
from tkinter import Button, Entry, Frame, Label

def open_window() -> None:
  window = globals.windows["main"]
  window.geometry("300x300")
  window.resizable(False,False)

  root = Frame(window) #type: ignore[annotation-unchecked]
  root.pack()

  create_header(root, "Lineares Gleichungssystem lösen")
  create_body(root)

  window.mainloop()

def create_body(root:Frame) -> None:
  body_frame:Frame = Frame(root)
  button_frame:Frame = Frame(body_frame)
  window_button_frame:Frame = Frame(body_frame)

  info_label:Label = Label(body_frame, text="Geben Sie hier Ihre lineare Funktion ein: ")
  solution_label:Label = Label(body_frame, font=("TKDefaultFont", 12))

  entry:Entry = Entry(body_frame)
  entry.bind("<Return>", lambda e: solve_button.invoke())

  solve_button:Button = Button(button_frame, text="Lösen", width=8)
  delete_button:Button = Button(button_frame, text="Löschen", width=8)
  test_button:Button = Button(button_frame, text="Test einfügen", width=8)

  create_graph_button:Button = Button(window_button_frame, text="Graphen anzeigen")
  create_pretty_button:Button = Button(window_button_frame, text="Formatierte Lösung anzeigen")

  body_frame.pack()
  info_label.pack()
  entry.pack()
  button_frame.pack(pady=4)
  solve_button.grid(row=0, column=0,  padx=4,)
  delete_button.grid(row=0, column=1,  padx=4)
  test_button.grid(row=0, column=2, padx=4)

  window_button_frame.pack(pady=4)
  create_graph_button.grid(row=0, column=0, padx=4)
  create_pretty_button.grid(row=0, column=1, padx=4)
  solution_label.pack()