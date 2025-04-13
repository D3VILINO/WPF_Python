from enum import Enum
import os
from tkinter import Entry, Frame, Label
from components import create_options
import passwordmanager as pwd

Typ = Enum("open", "create")

def get_database(frame_body:Frame, entry:Entry, header_label:Label, typ:Typ) -> None:
  database_name:str = entry.get()
  if typ == "create" and pwd.check_database(database_name) == False:
    database_name = pwd.create_database(database_name)
    header_label.config(text=database_name[:-4])
  elif typ == "open" and pwd.check_database(database_name) == False:
    header_label.config(text="Diese Datei existiert nicht")
  else:
    header_label.config(text=database_name)
  create_options(frame_body, header_label)

def create_database_folder() -> None:
  pwd_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pwd")
  if not os.path.isdir(pwd_dir):
    os.mkdir(pwd_dir)

def clear_frame(frame:Frame) -> None:
  for widget in frame.winfo_children():
    widget.destroy()