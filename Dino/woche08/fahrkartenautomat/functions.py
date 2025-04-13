from tkinter import *

def create_header(frame:Frame) -> Label:
  frame_header:Frame = Frame(frame)
  frame_header.pack()

  header:Label = Label(frame_header, padx=5, text="="*21, font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)

  header = Label(frame_header, padx=5, text="Fahrkartenautomat", font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)
  header_label = header

  header = Label(frame_header, padx=5, text="="*21, font=("Helvetica", 20))
  header.pack(fill=BOTH, expand=TRUE, anchor=N)
  return header_label

def clear_frame(frame:Frame) -> None:
  for widget in frame.winfo_children():
    widget.destroy()

def create_start(frame:Frame) -> None:
  clear_frame(frame)

  tickets:dict[str, int] = {
    "Einzelfahrschein AB": 380,
    "Einzelfahrschein BC": 380,
    "Einzelfahrschein ABC": 430,
    "Kurzstrecke AB": 250,
    "Tageskarte AB": 890,
    "Tageskarte ABC": 1020,
    "4-Fahrten-Karte AB": 960,
}

  button_frame:Frame = Frame(frame)
  button_frame.pack()
  for i in range(len(tickets)):
    ticket_name, price = list(tickets.items())[i]
    Button(button_frame, text=ticket_name, command=lambda l_price=price: pay(frame,ticket_name, l_price)).grid(row=i//2, column=i%2, sticky="w", padx=5, pady=2)

def pay(frame:Frame, name:str, to_pay_int:int=0) -> None:
  clear_frame(frame)
  possible_money = (200, 100, 50, 20, 10, 5)

  def process_money(i:int) -> None:
    nonlocal to_pay_int
    to_pay_int -= i
    to_pay_label.config(text=price_to_text(to_pay_int))
    if to_pay_int <= 0:
      create_endscreen(frame, name, abs(to_pay_int))

  label:Label = Label(frame, text="Zu zahlen", font=("Helvetica", 16))
  label.grid(row=0, column=0)
  to_pay_label:Label = Label(frame, text=price_to_text(to_pay_int), font=("Helvetica", 16))
  to_pay_label.grid(row=0, column=1)


  for i in range(len(possible_money)):
    Button(frame, text=price_to_text(possible_money[i]), command=lambda i=possible_money[i]:process_money(i)).grid(row=1+i, column=0, columnspan=2)

def price_to_text(i:int) -> str:
    return f"{i/100:.2f}€"

def create_endscreen(frame:Frame, name:str, exchange:int) -> None:
  clear_frame(frame)

  Label(frame, text=f"You bought {name}", font=("Helvetica", 16)).pack()
  if exchange > 0:
    exchange_text = f"Your exchange is {price_to_text(exchange)} in:\n"
    while exchange >= 200:
      exchange_text += "2 EURO\n"
      exchange -= 200
    if exchange >= 100:
      exchange_text += "1 EURO\n"
      exchange -= 100
    if exchange >= 50:
      exchange_text += "50 CENT\n"
      exchange -= 50
    if exchange >= 20:
      exchange_text += "20 CENT\n"
      exchange -= 20
    if exchange >= 10:
      exchange_text += "10 CENT\n"
      exchange -= 10
    if exchange >= 5:
      exchange_text += "5 CENT\n"
      exchange -= 5
    Label(frame, text=exchange_text).pack()

  frame.after(3000, create_start, frame)
