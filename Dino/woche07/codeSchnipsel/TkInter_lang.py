import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  #vorher Python Image Preview installieren
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hier steht der Titel!")
    root.geometry("400x400")
    #root.minsize(width=250, height=250)
    #root.maxsize(width=600, height=600)
    #root.resizable(width=False, height=True)

    style = ttk.Style()
    style.theme_use("clam")

    label1 = tk.Label(root, text="Label 1", bg="green")
    label1.pack(side="top",  fill="y", expand=True)    # "bottom", "left", "right" möglich

    label2 = tk.Label(root, text="Label 2", bg="red")
    label2.pack(side="top", fill="both", expand=True)

    image = Image.open("auto.png").resize((100, 100))
    photo = ImageTk.PhotoImage(image)

    label3 = ttk.Label(root, text="Mein Text.", image=photo, compound="bottom", padding=50)
    label3.pack()
    label3.configure(font=("Courier", 30), background="pink")

    for item in label3.keys():          # liefert alle Attributwerte für label3
        print(item, ": ", label3[item])
    
    # Variablen in TkInter (StringVar, IntVar, DoubleVar, ...)
    # gelten für root gesamt, z.B. wird text_variable in Zeile 38 in die GUI
    # gepackt und erst danach aktualisiert (Zeile 40)
    text_variable = tk.StringVar()  
    text_variable.set("Das ist der neue Text.")

    label4 = ttk.Label(root, textvariable=text_variable)
    label4.pack()

    text_variable.set("Aktualisierter Text.")


    root.mainloop()