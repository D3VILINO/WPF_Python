import json
import os
from tkinter import END, Entry

# man könnte verschiedenen usern verschiedene json geben 
test_file = os.path.join(os.path.curdir,  "json", "testuser.json")

# könnte man beim aktivieren stattdessen auch löschen (pop), aber ein extra button mit "lösche fertige" wäre schöner gewesen
def toggle_done(index:int) -> None:
  global test_file
  with open(test_file, "r") as f:
    data = json.load(f)

  data["done"][index] = 1 if data["done"][index] == 0 else 0

  with open(test_file, "w") as f:
    json.dump(data, f)

def add_todo(todo_entry:Entry) -> None:
  global test_file
  todo = todo_entry.get()
  with open(test_file, "r") as f:
    json_data = json.load(f)

  json_data["content"].append(todo)
  json_data["done"].append(0)

  with open(test_file, "w") as f:
    json.dump(json_data, f)
    todo_entry.delete(0, END)

# man könnte verschiedenen usern verschiedene json geben 
def initialize_json() -> None:
  global test_file
  dir = os.path.join(os.path.curdir,  "json")

  if not os.path.exists(dir):
    os.mkdir(dir)

  if not os.path.exists(test_file):
    with open(test_file, "w") as f:
      # Auf die schnelle 5 tests bei nicht vorhandener datei, weil es sonst erst garnicht startet :(
      json.dump({"content": ["test1", "test2", "test3", "test4", "test5"], "done": [0,0,0,0,0]}, f)