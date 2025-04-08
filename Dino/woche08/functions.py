from enum import Enum
from tkinter import Entry, Label
import passwordmanager as pwd

Typ = Enum("open", "create")

def get_database(entry:Entry, header_label:Label, typ:Typ) -> None:
  database_name:str = entry.get()
  if typ == "create" and pwd.check_database(database_name) == False:
    database_name = pwd.create_database(database_name)
    header_label.config(text=database_name[:-4])
  elif typ == "open" and pwd.check_database(database_name) == False:
    header_label.config(text="Diese Datei existiert nicht")
  else:
    header_label.config(text=database_name)

