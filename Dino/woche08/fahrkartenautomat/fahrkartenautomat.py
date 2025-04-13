import time

def main(args):
    zu_zahlen = fahrkarte_waehlen()
    rueckgabebetrag = geld_einwerfen(zu_zahlen)
    fahrkarte_ausgeben()
    rueckgeld_ausgeben(rueckgabebetrag)

def fahrkarte_waehlen():
    print("Zu zahlender Betrag (EURO): ", end = "")
    return float(input())

def geld_einwerfen(zu_zahlen):
    zu_zahlender_betrag = zu_zahlen
    eingezahlter_gesamtbetrag = 0.0
    while eingezahlter_gesamtbetrag < zu_zahlender_betrag:
        print("Noch zu zahlen: %.2f" %(zu_zahlender_betrag - eingezahlter_gesamtbetrag))
        print("Eingabe (mind. 5Ct, höchstens 2 Euro): ", end = "")
        eingeworfene_münze = float(input())
        eingezahlter_gesamtbetrag += eingeworfene_münze
    return eingezahlter_gesamtbetrag - zu_zahlender_betrag


def fahrkarte_ausgeben():
    print("\nFahrschein wird ausgegeben")
    for i in range(0, 8, 1):
        print("=", end = "")
        time.sleep(0.25)
    print("\n\n")

def rueckgeld_ausgeben(rueckgabebetrag):
    if rueckgabebetrag > 0.0:
        print("Der rueckgabebetrag in Höhe von %.2f EURO" %rueckgabebetrag)
        print("wird in folgenden Münzen ausgezahlt:")

        while rueckgabebetrag >= 2.0: # 2 EURO-Münzen
            print("2 EURO")
            rueckgabebetrag -= 2.0
        while rueckgabebetrag >= 1.0: # 1 EURO-Münzen
            print("1 EURO")
            rueckgabebetrag -= 1.0
        while rueckgabebetrag >= 0.5: # 50 CENT-Münzen
            print("50 CENT")
            rueckgabebetrag -= 0.5
        while rueckgabebetrag >= 0.2: # 20 CENT-Münzen
            print("20 CENT")
            rueckgabebetrag -= 0.2
        while rueckgabebetrag >= 0.1: # 10 CENT-Münzen
            print("10 CENT")
            rueckgabebetrag -= 0.1
        while rueckgabebetrag >= 0.05: # 5 CENT-Münzen
            print("5 CENT")
            rueckgabebetrag -= 0.05

    print("\nVergessen Sie nicht, den Fahrschein\n"+
          "vor Fahrtantritt entwerten zu lassen!\n"+
          "Wir wünschen Ihnen eine gute Fahrt.\n")

while True:
  main("")