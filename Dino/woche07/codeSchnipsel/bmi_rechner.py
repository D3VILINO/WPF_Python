from tkinter import *

def calc_bmi():
    if gewicht.get() > 0 and groesse.get() > 0:
        bmi = gewicht.get() / (groesse.get()**2)
    else:
        labelBewertung.config(text="Bitte Gewicht und Größe eingeben")
        return
    if v.get() == "m":
        if bmi < 20:
            labelBewertung.config(text="Untergewicht")
        elif bmi < 25:
            labelBewertung.config(text="Normalgewicht")
        else: 
            labelBewertung.config(text="Übergewicht")
    elif v.get() == "w":
        if bmi < 19:
            labelBewertung.config(text="Untergewicht")
        elif bmi < 24:
            labelBewertung.config(text="Normalgewicht")
        else: 
            labelBewertung.config(text="Übergewicht")
    else:
        labelBewertung.config(text="Bitte Geschlecht angeben")
        labelBmi.config(text="")
        return
    labelBmi.config(text=round(bmi, 2))

window = Tk()
window.title("BMI-Rechner")
window.geometry('500x400')

# Frames
main_frame = Frame(window)
main_frame.pack(anchor=CENTER, expand=TRUE)

frameEingaben = Frame(main_frame)
frameEingaben.pack(anchor=CENTER, pady=20, expand=TRUE)

frameGeschlecht = Frame(frameEingaben)
frameGeschlecht.pack(anchor=CENTER, expand=TRUE)

frameResult = Frame(main_frame)
frameResult.pack(anchor=CENTER, expand=TRUE)

# Frame Eingaben
labelGeschlecht = Label(master=frameGeschlecht, text="Geschlecht", padx=5, pady=5)
labelGeschlecht.grid(row=0, column=0, columnspan=2)

v = StringVar(frameGeschlecht, "1")
radioButtonMann = Radiobutton(master=frameGeschlecht, text="männlich", variable=v, value="m")
radioButtonMann.grid(row=1, column=0, padx=5, pady=5)
radioButtonFrau = Radiobutton(master=frameGeschlecht, text="weiblich", variable=v, value="w")
radioButtonFrau.grid(row=1, column=1, padx=5, pady=5)

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
labelResult.grid(row=0, column=0, padx=5)

labelBmi = Label(master=frameResult, text='', font=('Helvetica', 14))
labelBmi.grid(row=0, column=1)

labelBewertung = Label(master=frameResult, text="", font=('Helvetica', 14))
labelBewertung.grid(row=1, column=0, columnspan=2)

window.mainloop()
