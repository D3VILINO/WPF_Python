from tkinter import *
from functions import add_solution, solve, test_import

def open_window():
  window:Tk = Tk() #type:ignore[annotation-unchecked]
  window.geometry("300x300")
  window.resizable(False,False)

  root:Frame = Frame(window) #type:ignore[annotation-unchecked]
  root.pack()

  create_header(root, "Lineares Gleichungssystem lösen")
  create_body_master(root)

  window.mainloop()


def create_header(root:Frame, text:str) -> None:
  header_frame:Frame = Frame(root)
  header_frame.pack(pady=20)

  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text=text, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()

def create_window_pretty(master, func):
  window = Toplevel(master) #type:ignore[annotation-unchecked]
  window.geometry("300x300")
  window.resizable(False,False)
  window.title("Formatierter Term")

  root:Frame = Frame(window) #type:ignore[annotation-unchecked]
  root.pack()

  create_header(root, "Formatierter Term")
  create_body_pretty(root, func)

  window.mainloop()

def create_body_pretty(root:Frame, func:str) -> None:
  body_frame:Frame = Frame(root)
  body_frame.pack()

  pretty_label:Label = Label(body_frame, font=("TKDefaultFont", 12))
  text:str = add_solution(func, pretty_label, do_pretty=True) or "Es gab ein Programmfehler"
  pretty_label.config(text=text)
  pretty_label.pack()

def create_body_master(root:Frame) -> None:
  body_frame:Frame = Frame(root)
  button_frame:Frame = Frame(body_frame)
  window_button_frame:Frame = Frame(body_frame)

  info_label:Label = Label(body_frame, text="Geben Sie hier Ihre lineare Funktion ein: ")
  solution:Label = Label(body_frame, font=("TKDefaultFont", 12))

  entry:Entry = Entry(body_frame)
  entry.bind("<Return>", lambda e: solve_button.invoke())

  solve_button:Button = Button(button_frame, text="Lösen", command=lambda:add_solution(entry.get().replace(" ", ""), solution), width=8)
  delete_button:Button = Button(button_frame, text="Löschen", command=lambda: entry.delete(0, END), width=8)
  test_button:Button = Button(button_frame, text="insert", command=lambda: test_import(entry), width=8)


  create_graph_button:Button = Button(window_button_frame, text="Graphen anzeigen")
  create_pretty_button:Button = Button(window_button_frame, text="Formatierte Lösung anzeigen", command=lambda: create_window_pretty(root, entry.get()))

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
  solution.pack()
