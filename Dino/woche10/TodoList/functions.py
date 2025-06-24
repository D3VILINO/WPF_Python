import json
import os
from tkinter import END, Entry


def add_todo(todo_entry:Entry) -> None:
  initialize_json()
  todo = todo_entry.get()
  test_file = os.path.join(os.path.curdir,  "json", "testuser.json")
  with open(test_file, "r") as json_file:
    json_data = json.load(json_file)

  json_data["content"].append(todo)

  with open(test_file, "w") as json_file:
    json.dump(json_data, json_file)
    todo_entry.delete(0, END)

def initialize_json() -> None:
  dir = os.path.join(os.path.curdir,  "json")
  test_file = os.path.join(os.path.curdir,  "json", "testuser.json")

  if not os.path.exists(dir):
    os.mkdir(dir)

  if not os.path.exists(test_file):
    with open(test_file, "w") as test_file:
      json.dump({"content": []}, test_file)