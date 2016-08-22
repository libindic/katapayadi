from .core import Katapayadi

def katapayadi_getnumber(word):
    return Katapayadi().get_number(word)

def getnumber():
    return [katapayadi_getnumber, str, int]

