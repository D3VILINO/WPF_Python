from tkinter import Button, Entry, Frame

def create_calculator(master:Frame) -> None:
  _create_display(master)
  _create_left_collumn(master)
  _create_body(master)

def _create_display(master:Frame) -> None:
  label_display = Entry(master, state="disabled", width=30)
  label_display.pack(pady=10)

def _create_left_collumn(master:Frame) -> None:
  frame_left_column = Frame(master)
  frame_left_column.pack(side="left")

  label_what = Entry(frame_left_column, state="disabled", font=("Helvetica", 16), width=2)
  label_what.pack(pady="7")

  buttons_memory = ("MC", "MR", "MS", "M+")
  for text in buttons_memory:
    button = Button(frame_left_column, text=text, borderwidth=5)
    button.pack(pady="1")

def _create_body(master:Frame) -> None:
  frame_body = Frame(master)
  frame_body.pack()

  # Comands
  top_row = (("Backspace", 0), ("CE", 5), ("C", 10))
  for text, column in top_row:
    button = Button(frame_body, text=text, width=8, borderwidth=5)
    button.grid(row=0, column=column, columnspan=5, padx=1, pady=5, sticky="ew")

  # Inputs
  frame_inputs = Frame(frame_body)
  frame_inputs.grid(row=1, column=0, columnspan=15, rowspan=3, sticky="ew")
  
  for i in range(0,9):
    button = Button(frame_inputs, text=f"{i+1}", borderwidth=5, command=_add_to_display)
    button.grid(row=2-(i//3), column=i%3, padx=1, pady=1, sticky="ew")
  
  bottom_row = (("0", 0), ("+/-", 1), (".", 2))
  for text, column in bottom_row:
    button = Button(frame_inputs, text=text, borderwidth=5, command=_add_to_display)
    button.grid(row=3, column=column, padx=1, pady=1, sticky="ew")
  
  right_columns = (("/", 0, 3), ("Sqrt", 0, 4), ("*", 1, 3), ("%", 1, 4), ("-", 2, 3), ("1/x", 2, 4), ("+", 3, 3), ("=", 3, 4))
  for text, row, column in right_columns:
    button = Button(frame_inputs, text=text, borderwidth=5, command=_add_to_display)
    button.grid(row=row, column=column, padx=1, pady=1, sticky="ew")

  for i in range(5):
    frame_inputs.columnconfigure(i, weight=1)

def _add_to_display():
  pass
  