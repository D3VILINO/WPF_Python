from tkinter import * # type: ignore
from functions import * # type: ignore

current_page:int = 0

def open_window():
  initialize_json()
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
  global current_page, test_file
  checkbox_list:list[tuple[Checkbutton, BooleanVar]] = []
  body_frame:Frame = Frame(root)
  checkbox_frame:Frame = Frame(body_frame)
  button_frame:Frame = Frame(body_frame)


  info_label:Label = Label(body_frame, text="Geben Sie hier Ihre Aufgabe ein: ")
  todo_entry:Entry = Entry(body_frame)
  add_button:Button = Button(body_frame, text="Hinzufügen", width=8, command=lambda:add_todo(todo_entry))
  todo_entry.bind("<Return>", lambda e: add_button.invoke())
  previous_button:Button = Button(button_frame, text="Zurück", width=8, command=lambda: change_page("back", checkbox_list, current_page_label))
  next_button:Button = Button(button_frame, text="Weiter", width=8, command=lambda:change_page("next", checkbox_list, current_page_label))
  current_page_label:Label = Label(button_frame, text=str(current_page+1))

  for i in range(current_page*5, current_page*5 + 5):
    with open(test_file, "r") as f:
      data = json.load(f)
      done_list = data["done"]
      content_list = data["content"]
    var = BooleanVar(value=(done_list[i + current_page*5] == 1))
    tasks_ckeckbox:Checkbutton = Checkbutton(checkbox_frame, text=content_list[i + current_page*5], variable=var, command=lambda index=i: toggle_done(index + current_page*5)) #type: ignore
    tasks_ckeckbox.pack(side="top", anchor="w")
    checkbox_list.append((tasks_ckeckbox, var))

  body_frame.pack(fill="x")
  info_label.pack()
  todo_entry.pack()
  add_button.pack()
  todo_entry.pack()

  checkbox_frame.pack()

  button_frame.pack(fill="both")
  previous_button.pack(side="left")
  current_page_label.pack(side="left", expand=True)
  next_button.pack(side="right")

def change_page(direction:str, checkbox_list:list[tuple[Checkbutton, BooleanVar]], page_label:Label) -> None:
  global current_page
  current_page = current_page + 1 if direction == "next" else current_page - 1  
  test_file = os.path.join(os.path.curdir,  "json", "testuser.json")
  
  for i in range(len(checkbox_list)):
    with open(test_file, "r") as f:
      data = json.load(f)
      content_list = data["content"]
      done_list = data["done"]
      if current_page < 0:
        current_page += 1
        return
      elif len(content_list) - 1 < current_page*5:
        current_page -= 1
        return
      try:
        var =(done_list[i + current_page*5] == 1)
        checkbox_list[i][1].set(var)
        checkbox_list[i][0].config(state="normal", text=content_list[i + current_page*5])
      except IndexError:
        checkbox_list[i][0].config(state="disabled", text="Nichts")
  page_label.configure(text=current_page+1)
  