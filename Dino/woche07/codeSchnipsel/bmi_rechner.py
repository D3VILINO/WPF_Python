from tkinter import *

def calc_bmi():
    labelBmi.config(text=round(gewicht.get()/ groesse.get()**2,2))

window = Tk()
window.title("BMI-Rechner")
window.geometry('300x300')

# Frames
main_frame = Frame(window)
main_frame.pack(expand=TRUE, fill=BOTH)

frameEingaben = Frame(main_frame)
frameEingaben.pack(fill=BOTH, expand=TRUE, pady=20)

frameResult = Frame(main_frame)
frameResult.pack(fill=BOTH, anchor=N, expand=TRUE)

# Frame Eingaben
labelGeschlecht = Label(master=frameEingaben, text="Geschlecht", padx=5, pady=5)
labelGeschlecht.pack(anchor=N)

v = StringVar(frameResult, "1")
radioButtonMann = Radiobutton(master=frameEingaben, text="männlich", variable=v, value="m")
radioButtonMann.pack(anchor=N, side=LEFT, padx=5, pady=5)

labelGewicht = Label(master=frameEingaben, text='Gewicht in kg:', padx=5, pady=5)
labelGewicht.pack(anchor=N)

gewicht = IntVar()
entryGewicht = Entry(master=frameEingaben, textvariable=gewicht)
entryGewicht.pack(anchor=N, padx=5, pady=5)

labelGroesse = Label(master=frameEingaben, text='Größe in m:', padx=5, pady=5)
labelGroesse.pack(anchor=N)

groesse = DoubleVar()
entryGroesse = Entry(master=frameEingaben, textvariable=groesse)
entryGroesse.pack(anchor=N, padx=5, pady=5)

button = Button(master=frameEingaben, text='berechnen', command=calc_bmi)
button.pack(anchor=N, padx=5, pady=5)

# Frame Result
labelResult = Label(master=frameResult, text='BMI:', font=('Helvetica', 14))
labelResult.pack(anchor=N, side=LEFT, expand=True)

labelBmi = Label(master=frameResult, text='', font=('Helvetica', 14))
labelBmi.pack(anchor=N, side=LEFT, expand=True)

window.mainloop()
