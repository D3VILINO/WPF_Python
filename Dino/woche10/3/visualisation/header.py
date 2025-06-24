from tkinter import Frame, Label


def create_header(root:Frame, text:str) -> None:
  header_frame:Frame = Frame(root)
  header_frame.pack(pady=20)

  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text=text, font=("TKDefaultFont", 12)).pack()
  Label(header_frame, text="="*30, font=("TKDefaultFont", 12)).pack()