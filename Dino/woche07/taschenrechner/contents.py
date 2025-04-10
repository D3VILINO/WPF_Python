from imports.contents import *

label_display:Label
label_what:Label

def create_calculator(master:Frame) -> None:
  _create_display(master)
  _create_left_collumn(master)
  _create_body(master)

def _create_display(master:Frame) -> None:
  global label_display
  frame_display = Frame(master, bg="black")
  frame_display.pack()
  label_display = Label(frame_display, width=30, bg="white")
  label_display.pack(padx=1, pady=1)

def _create_left_collumn(master:Frame) -> None:
  global label_what
  frame_left_column = Frame(master)
  frame_left_column.pack(side="left")

  label_what = Label(frame_left_column, state="disabled", font=("Helvetica", 16), width=2)
  label_what.pack(pady="7")

  buttons_memory = ("MC", "MR", "MS", "M+")
  for text in buttons_memory:
    button = Button(frame_left_column, text=texth, borderwidt=5, command=partial(_add_to_display, text))
    button.pack(pady="1")

def _create_body(master:Frame) -> None:
  frame_body = Frame(master)
  frame_body.pack()

  top_row = (("Backspace", 0), ("CE", 5), ("C", 10))
  for text, column in top_row:
    button = Button(frame_body, text=text, width=8, borderwidth=5, command=partial(_delete_from_display, text))
    button.grid(row=0, column=column, columnspan=5, padx=1, pady=5, sticky="ew")

  frame_inputs = Frame(frame_body)
  frame_inputs.grid(row=1, column=0, columnspan=15, rowspan=3, sticky="ew")

  for i in range(0,9):
    button = Button(frame_inputs, text=f"{i+1}", borderwidth=5, command=partial(_add_to_display, str(i+1)))
    button.grid(row=2-(i//3), column=i%3, padx=1, pady=1, sticky="ew")

  bottom_row = (("0", 0), ("+/-", 1), (".", 2))
  for text, column in bottom_row:
    button = Button(frame_inputs, text=text, borderwidth=5, command=partial(_add_to_display, text))
    button.grid(row=3, column=column, padx=1, pady=1, sticky="ew")

  right_columns = (("/", 0, 3), ("Sqrt", 0, 4), ("*", 1, 3), ("%", 1, 4), ("-", 2, 3), ("1/x", 2, 4), ("+", 3, 3), ("=", 3, 4))
  for text, row, column in right_columns:
    button = Button(frame_inputs, text=text, borderwidth=5, command=partial(_add_to_display, text))
    button.grid(row=row, column=column, padx=1, pady=1, sticky="ew")

  for i in range(5):
    frame_inputs.columnconfigure(i, weight=1)

def _add_to_display(s:str) -> None:
  global label_display
  global label_what
  label_text:str = label_display.cget("text")
  label_what.config(text="")
  try:
    match s:
      case "+/-":
        label_display.config(text=change_plus_minus(label_text))
      case ".":
        label_display.config(text=check_for_dots(label_text))
      case "Sqrt":
        label_display.config(text=toggle_sqrt(label_text))
      case "%":
        label_display.config(text=into_percent(label_text))
      case "1/x":
        label_display.config(text=divide_by(label_text))
      case "=":
        label_display.config(text=str(eval(label_text)))
      case _:
        label_display.config(text=label_text+s)
  except:
    label_what.config(text="Err")

def _delete_from_display(s:str) -> None:
  global label_display
  match s:
    case "C":
      label_display.config(text="")
    case "CE":
      label_display.config(text="") # keine Funktion zwischenrechnungen zu speichern
    case "Backspace":
      text = label_display.cget("text")
      if text == "":
        return
      if text[-1] == "t":
        label_display.config(text=text[0:-4])
      else:
        label_display.config(text=text[0:-1])
