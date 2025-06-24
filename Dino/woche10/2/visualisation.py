from tkinter import END, Frame, Label, Tk, Toplevel, Entry, Button
from matplotlib import pyplot as plt
import numpy as np
import functions as fnc

windows:dict[str,Tk|Toplevel] = {"main":Tk()} #type: ignore[annotation-unchecked]

def open_window():
  global windows
  window:Tk = windows["main"] #type: ignore[annotation-unchecked]
  window.geometry("300x300")
  window.resizable(False,False)

  root:Frame = Frame(window) #type: ignore[annotation-unchecked]
  root.pack()

  create_header(root, "Lineares Gleichungssystem lösen")
  create_body_main(root)

  window.mainloop()

def create_header(root:Frame, text:str) -> None:
  header_frame:Frame = Frame(root)
  header_frame.pack(pady=20)

  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text=text, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()

def create_window_pretty(func):
  pass

def create_window_graph() -> None:
  global windows
  window:Toplevel = Toplevel(windows["main"]) #type: ignore[annotation-unchecked]
  windows["graph"] = window
  window.geometry("300x300")
  window.resizable(False,False)
  window.title("Grafische Lösung")

  root:Frame = Frame(window) #type: ignore[annotation-unchecked]
  root.pack()

  create_header(root, "Grafische Lösung")
  create_body_graph(root)

  window.mainloop()

def create_body_graph(root:Frame) -> None:
  body_frame:Frame = Frame(root)

  x = np.linspace(-10, 10, 200, endpoint=True)
  akk = fnc.solution[1]
  f1 = f"{akk}"
  plt.plot(x, f1)
  plt.show()

def create_body_main(root:Frame) -> None:
  body_frame:Frame = Frame(root)
  button_frame:Frame = Frame(body_frame)
  window_button_frame:Frame = Frame(body_frame)

  info_label:Label = Label(body_frame, text="Geben Sie hier Ihre lineare Funktion ein: ")
  solution_label:Label = Label(body_frame, font=("TKDefaultFont", 12))

  entry:Entry = Entry(body_frame)
  entry.bind("<Return>", lambda e: solve_button.invoke())

  solve_button:Button = Button(button_frame, text="Lösen", width=8, command=lambda:fnc.submitted_entry(entry.get(), solution_label))
  delete_button:Button = Button(button_frame, text="Löschen", command=lambda: entry.delete(0, END), width=8)
  test_button:Button = Button(button_frame, text="insert", command=lambda: fnc.test_import(entry), width=8)


  create_graph_button:Button = Button(window_button_frame, text="Graphen anzeigen", command=create_window_graph)
  create_pretty_button:Button = Button(window_button_frame, text="Formatierte Lösung anzeigen", command=lambda: create_window_pretty(entry.get()))

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
