from enum import Enum
from functools import partial
import os
from tkinter import Button, Entry, Frame, Label
from components import *

Typ = Enum("open", "create")

def get_database(frame_body:Frame, entry:Entry, header_label:Label, typ:Typ) -> None:
  database_name:str = entry.get()
  if typ == "create" and check_database(database_name) == False:
    database_name = create_database(database_name)
    header_label.config(text=database_name[:-4])
  elif typ == "create" and check_database(database_name) == True:
    header_label.config(text="Diese Datenbank existiert bereits")
    return
  elif typ == "open" and check_database(database_name) == False:
    header_label.config(text="Diese Datei existiert nicht")
    return
  else:
    header_label.config(text=database_name)
  create_options(frame_body, header_label)

def get_database_path(database_name:str) -> str:
  return os.path.join(os.path.dirname(os.path.abspath(__file__)), "pwd", database_name + ".txt")

def create_options(frame_body:Frame, header_label:Label) -> None:
  clear_frame(frame_body)

  button:Button
  button = Button(frame_body, text="Show existing passwords", padx=5, font=("Helvetica", 16), command=partial(create_password_list, frame_body, header_label))
  button.pack()

  button = Button(frame_body, text="Add new password", padx=5, font=("Helvetica", 16), command=partial(create_add_password, frame_body, header_label))
  button.pack()

  button = Button(frame_body, text="Delete an existing password", padx=5, font=("Helvetica", 16), command=lambda: create_delete_password(frame_body, header_label))
  button.pack()

  button = Button(frame_body, text="Update password", padx=5, font=("Helvetica", 16))
  button.pack()

  button = Button(frame_body, text="Return", padx=5, font=("Helvetica", 16), command=partial(create_start, frame_body, header_label))
  button.pack()

def create_delete_password(frame_body:Frame, header_label:Label) -> None:
  clear_frame(frame_body)

  table_header = Label(frame_body, text="Index, Name, Password, URL, Note")
  table_header.pack()

  database = get_database_path(header_label.cget("text"))
  file = open(database, "r")
  lines = file.readlines()
  for i in range(len(lines) - 1):
    data = lines[i + 1].strip().split(";")
    line = ""
    for d in data:
      line += d + ", "
    line = line[:-2]
    password = Label(frame_body, text=line)
    password.pack()

  label_index = Label(frame_body, text="Index of deleting Password")
  label_index.pack()
  index_entry = Entry(frame_body)
  index_entry.pack()

  delete_button = Button(frame_body, text="Delete", command=lambda: delete_password(index_entry.get(), database, frame_body, header_label))
  delete_button.pack()

  return_button:Button = Button(frame_body, text="Return", padx=5, font=("Helvetica", 16), command=partial(create_options, frame_body, header_label))
  return_button.pack()

def delete_password(index:str, database:str, frame_body:Frame, header_label:Label):
  file = open(database, "r")
  lines = file.readlines()
  file.close()

  del lines[int(index)]

  for i in range(1, len(lines)):
    line = lines[i].strip().split(";")
    if line:
      line[0] = str(i)  # Neue Indexnummer
      lines[i] = ";".join(line) + "\n"

  file = open(database, "w")
  file.writelines(lines)
  file.close()
  create_delete_password(frame_body, header_label)

def create_password_list(frame_body:Frame, header_label:Label) -> None:
  clear_frame(frame_body)

  table_header = Label(frame_body, text="Index, Name, Password, URL, Note")
  table_header.pack()

  database = get_database_path(header_label.cget("text"))
  file = open(database, "r")
  lines = file.readlines()
  for i in range(len(lines) - 1):
    data = lines[i + 1].strip().split(";")
    line = ""
    for d in data:
      line += d + ", "
    line = line[:-2]
    password = Label(frame_body, text=line)
    password.pack()
  return_button:Button = Button(frame_body, text="Return", padx=5, font=("Helvetica", 16), command=partial(create_options, frame_body, header_label))
  return_button.pack()

def create_add_password(frame_body:Frame, header_label:Label) -> None:
  clear_frame(frame_body)

  data_row = {"Index": "", "Name": "", "Password": "", "URL": "", "Note": ""}
  data_row.update({"Index": str(number_of_lines(get_database_path(header_label.cget("text"))))})

  name_label = Label(frame_body, text="Name")
  name_label.pack()
  name_entry = Entry(frame_body)
  name_entry.pack()

  password_label = Label(frame_body, text="Password")
  password_label.pack()
  password_entry = Entry(frame_body)
  password_entry.pack()

  url_label = Label(frame_body, text="URL")
  url_label.pack()
  url_entry = Entry(frame_body)
  url_entry.pack()

  note_label = Label(frame_body, text="Note")
  note_label.pack()
  note_entry = Entry(frame_body)
  note_entry.pack()

  add_button = Button(frame_body, text="add", command=lambda: add_password(get_database_path(header_label.cget("text")), name_entry.get(), password_entry.get(), url_entry.get(), note_entry.get()))
  add_button.pack()
  return_button = Button(frame_body, text="return", command=partial(create_options, frame_body, header_label))
  return_button.pack()

def add_password(database:str, name:str, pwd:str, url:str, note:str):
  file = open(database, "a")
  file.write(f"{number_of_lines(database)};{name};{pwd};{url};{note}")
  file.close()

  file = open(database, "r")
  content = file.read()
  file.close()

  content = content[:-1]

  file = open(database, "w")
  file.write(content + "\n")
  file.close()

def number_of_lines(database) -> int:
  """Including the header"""
  file = open(database, "r")
  akk = 0
  for _ in file:
    akk += 1
  file.close()
  return akk

def create_database_folder() -> None:
  pwd_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pwd")
  if not os.path.isdir(pwd_dir):
    os.mkdir(pwd_dir)

def create_start(frame_body:Frame, header_label:Label) -> None:
  clear_frame(frame_body)

  entry:Entry = Entry(frame_body, text="New Database", font=("Helvetica", 16))
  entry.grid(row=0, column=0, columnspan=3, padx=5, pady=20)

  button:Button = Button(frame_body, text="New Database", padx=5, font=("Helvetica", 16), command=partial(get_database, frame_body, entry, header_label, "create"))
  button.grid(row=1, column=0, padx=5)
  button = Button(frame_body, text="Open Database", padx=5, font=("Helvetica", 16), command=partial(get_database, frame_body, entry, header_label, "open"))
  button.grid(row=1, column=1, padx=5)
  button = Button(frame_body, text="Exit", padx=5, font=("Helvetica", 16), command=exit)
  button.grid(row=1, column=2, padx=5)

def clear_frame(frame:Frame) -> None:
  for widget in frame.winfo_children():
    widget.destroy()

def check_database(database: str) -> bool:
  return os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pwd", database + ".txt"))

def create_database(name:str|None) -> str:
  database = name
  if not database.__contains__(".txt"): # keine gute, aber wenigstens irgendeine Überprüfung
      database += ".txt"
      file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pwd", database), "w")
      file.write("Index;Name;Password;URL;Note\n")
      file.close()
  return database