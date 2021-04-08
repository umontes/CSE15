from logic import TruthTable
import sys

def equi():

    print("Proposition equivalence")
    print("|1 = not p    || 2 = not q   || 3 = p and q || 4 = q and p |")
    print("|5 = p or q   || 6 = q or p  || 7 = p -> q  || 8 = q -> p  |")
    print("|9 = p <-> q  || 10 = q <-> p |\n")

    prop1 = int(raw_input("Enter Proposition 1: "))
    prop2 = int(raw_input("Enter Proposition 2: "))

    if(prop1 == 1 and prop2 == 2) or (prop1 == 2 and prop2 == 1):
      print("The propositions are not equivalent")
      equi()
    if(prop1 == 3 and prop2 == 4) or (prop1 == 4 and prop2 == 3):
      print("The propositions are equivalent")
      equi()
    if(prop1 == 5 and prop2 == 6) or (prop1 == 6 and prop2 == 5):
      print("The propositions are equivalent")
      equi()
    if(prop1 == 7 and prop2 == 8) or (prop1 == 8 and prop2 == 7):
      print("The propositions are equivalent")
      equi()
    if(prop1 == 9 and prop2 == 10) or (prop1 == 10 and prop2 == 9):
      print("The propositions are equivalent")
      equi()

    else:
      print("Incorrect propositions!")
      equi()

equi()