print("1. feladat:")
szoveg = input("Kérek egy szöveget: ")
szam = input("Kérek egy egész számot: ")

while not szam.isnumeric():
    print("Ez nem egész szám!")
    szam = input("Kérek egy egész számot: ")

szam = int(szam)

if szam > len(szoveg):
    print("Sajnos nincs ilyen betű.")
else:
    print(szoveg[szam]*szam)