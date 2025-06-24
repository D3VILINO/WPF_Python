from typing import Any
from sympy import Symbol
from tkinter import Tk, Toplevel

#visual
windows:dict[str,Tk|Toplevel] = {"main":Tk()} #type: ignore[annotation-unchecked]

# math
x:Symbol
y:Symbol
solution:Any
f1:Any