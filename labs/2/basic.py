from logic import TruthTable
import sys

def basic():

    print("|1 = not a    || 2 = not b   || 3 = a and b || 4 = b and a |")
    print("|5 = a or b   || 6 = b or a  || 7 = a -> b  || 8 = b -> a  |")
    print("|9 = a <-> b  || 10 = b <-> a |\n")
    
    prop = int(raw_input("Choose a proposition: "))
    
    if prop == 1:
        myTable = TruthTable(['a','b'], ['-a'])
        myTable.display()
        print("\n")
        basic()
    if prop == 2:
        myTable = TruthTable(['a','b'], ['-b'])
        myTable.display()
        print("\n")
        basic()
    if prop == 3:
        myTable = TruthTable(['a','b'], ['a and b'])
        myTable.display()
        print("\n")
        basic()
    if prop == 4:
        myTable = TruthTable(['a','b'], ['b and a'])
        myTable.display()
        print("\n")
        basic()
    if prop == 5:
        myTable = TruthTable(['a','b'], ['a or b'])
        myTable.display()
        print("\n")
        basic()
    if prop == 6:
        myTable = TruthTable(['a','b'], ['b or a'])
        myTable.display()
        print("\n")
        basic()
    if prop == 7:
        myTable = TruthTable(['a','b'], ['a -> b'])
        myTable.display()
        print("\n")
        basic()
    if prop == 8:
        myTable = TruthTable(['a','b'], ['b -> a'])
        myTable.display()
        print("\n")
        basic()
    if prop == 9:
        myTable = TruthTable(['a','b'], ['a <-> b'])
        myTable.display()
        print("\n")
        basic()
    if prop == 10:
        myTable = TruthTable(['a','b'], ['b <-> a'])
        myTable.display()
        print("\n")
        basic()
    
    else:
        print("Not a correct prop!\n")
        basic()
        
basic()