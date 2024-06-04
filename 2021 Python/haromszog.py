#def haromszog():
#    a = int(input("Kérem a(z) 1. egész számot: "))
#    b = int(input("Kérem a(z) 2. egész számot: "))
#    c = int(input("Kérem a(z) 3. egész számot: "))
#    return [a,b,c]

def haromszog():
    szamok = []
    for a in range(3):
        while True:
            try:
                x = int(input(f"Kérem a(z) {a+1}. egész számot: "))
            except:
                print("Ez nem egész szám!")
            else:
                szamok.append(x)
                break
    return szamok