from haromszog import *

def haromszogek():
    haromszogAdatai = []
    for bekeres in range(3):
        print(f"{bekeres+1}. adatsor")
        haromszogAdatai.append(haromszog())
    for egyHaromszog in haromszogAdatai:
        print(f"\ta={egyHaromszog[0]}, b={egyHaromszog[1]}, c={egyHaromszog[2]}")
    return haromszogAdatai

def ellenorzes(egyLista):
    if egyLista[0] + egyLista[1] > egyLista[2] and egyLista[0] + egyLista[2] > egyLista[1] and egyLista[1] + egyLista[2] > egyLista[0]:
        return True
    else:
        return False


haromszogLista = haromszogek()
for i, haromszogOldalai in enumerate(haromszogLista):
    if ellenorzes(haromszogOldalai):
        print(f"{i+1}. számsor lehet háromszög")
    else:
        print(f"{i+1}. számsor nem lehet háromszög")