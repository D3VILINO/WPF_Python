from tkinter import *
from functions import *

def open_window():
  window:Tk = Tk() #type: ignore[annotation-unchecked]
  window.geometry("360x440")
  window.resizable(False,False)

  root:Frame = Frame(window) #type: ignore[annotation-unchecked]
  root.pack()

  create_header(root, "Todo List")
  create_body_main(root)

  window.mainloop()

def create_header(root:Frame, text:str) -> None:
  header_frame:Frame = Frame(root)
  header_frame.pack(pady=20)

  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text=text, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()

def create_body_main(root:Frame) -> None:
  body_frame:Frame = Frame(root)

  info_label:Label = Label(body_frame, text="Geben Sie hier Ihre Aufgabe ein: ")
  todo_entry:Entry = Entry(body_frame)
  add_button:Button = Button(body_frame, text="Hinzufügen", width=8, command=lambda:add_todo(todo_entry))
  todo_entry.bind("<Return>", lambda e: add_button.invoke())

  for i in range(3):
    tasks_ckeckbox:Checkbutton = Checkbutton(body_frame, text="test")
    tasks_ckeckbox.pack()

  info_label.pack()
  todo_entry.pack()
  add_button.pack()
  todo_entry.pack()
  body_frame.pack()