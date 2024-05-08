import math
from collections import namedtuple


Quantity = namedtuple("Quantity", "name, symbol, unit, unitabbr")


def output(t, l, r):

    '''
    Print details of the top, left and right Quantity arguments.
    Print a formula triangle using Quantity arguments
    Print the 3 individual formulas
    '''

    print("Quantity      Symbol      Unit\n")
    print(f"{t.name:<14}{t.symbol:<12}{t.unit} ({t.unitabbr})")
    print(f"{l.name:<14}{l.symbol:<12}{l.unit} ({l.unitabbr})")
    print(f"{r.name:<14}{r.symbol:<12}{r.unit} ({r.unitabbr})")

    print(f"\n     / \\")
    print(f"    /   \\")
    print(f"   /  {t.symbol}  \\")
    print(f"  / ----- \\")
    print(f" /  {l.symbol} ✕ {r.symbol}  \\")
    print(f"/___________\\\n")

    print(f"{t.symbol} = {l.symbol} ✕ {r.symbol}")
    print(f"{l.symbol} = {t.symbol} ÷ {r.symbol}")
    print(f"{r.symbol} = {t.symbol} ÷ {l.symbol}")


def evaluate(t: float, l: float, r: float) -> float:

    '''
    Calculate the missing "not a number"
    value from the two supplied values.
    Returns nan if arguments invalid.
    '''

    if math.isnan(t):
        return l * r
    elif math.isnan(l):
        return t / r
    elif math.isnan(r):
        return t / l
    else:
        return float('nan')
    
