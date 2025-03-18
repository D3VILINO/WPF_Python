
import tkinter as tk
from tkinter import messagebox

def hallo_sagen():
    tk.messagebox.showinfo(
        "Begrüßung",
        "Hallo"
    )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hallo Tkinter!")
    root.geometry("500x200")
    l1 = tk.Label(text="Test", fg="black", bg="white")
    button = tk.Button(
        root,
        text = "Drück mich!",
        command = hallo_sagen
    )
    button.pack()
    l1.pack()

    root.mainloop()