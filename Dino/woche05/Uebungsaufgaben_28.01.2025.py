class Stack:
  def __init__(self):
    self.st = []

  def push(self, value):
    self.st.append(value)

  def pop(self):
    return self.st.pop()

  def __len__(self):
    return len(self.st)

  def toList(self):
    return list(self.st)

  def multPop(self, n:int):
    popped = list()
    for i in range(n):
      popped.append(self.pop())
    return popped

s = Stack()
s.push(1); s.push("Hallo"); s.push(4.32); s.push(True)
print(s.pop())
print("--------")
s.push("a")
print(s.pop(), s.pop())
print(s.pop())
print("--------")
s.push(1); s.push("Hallo"); s.push(4.32); s.push(True)
print(s)
print("--------")
print(s.toList())
print("--------")
print(s.multPop(3))
print("--------")
print(s.__len__())

# ----------------------------------------------------------------
print("\n\nAufgabe 2")
class AufgabenManager:
  def __init__(self):
    self.aufgaben = {}

  def neueAufgabe(self, aufgabe:str, prioritaet:int):
    self.aufgaben[aufgabe] = prioritaet

  def hoechstePrio(self):
    minPrio = 9999999999999
    for prioritaet in self.aufgaben:
      if self.aufgaben[prioritaet] < minPrio:
        minPrio = self.aufgaben[prioritaet]
    return minPrio

  def erledigeNaechsteAufgabe(self):
    prio = self.hoechstePrio()
    aufgaben = []
    for aufgabe in self.aufgaben:
      if self.aufgaben[aufgabe] == prio:
        aufgaben.append(aufgabe)
    self.aufgaben.pop(aufgaben[-1])
    return aufgaben[-1]

  def anzahlAufgabenPrio(self, prio = 0):
    anzahl = 0
    for aufgabe in self.aufgaben:
      if prio == self.aufgaben[aufgabe]:
        anzahl += 1
    return anzahl

  def anzahlAufgaben(self):
    return len(self.aufgaben)

  def allePrios(self):
    print("Priorität: Anzahl")
    prios = {}
    for aufgabe in self.aufgaben:
      for prio in prios:
        if self.aufgaben[aufgabe] == prio:



aufgs = AufgabenManager()
aufgs.neueAufgabe("Kueche putzen", 5)
aufgs.neueAufgabe("Auf Prog 1 lernen", 1)
aufgs.neueAufgabe("Oma besuchen", 2)
aufgs.neueAufgabe("Auf Mathe 1 lernen", 1)
aufgs.neueAufgabe("Fahrrad putzen", 10)
print(aufgs.erledigeNaechsteAufgabe ())
print(aufgs.erledigeNaechsteAufgabe ())
print(aufgs.hoechstePrio())
print(aufgs.anzahlAufgabenPrio())
print(aufgs.anzahlAufgaben())