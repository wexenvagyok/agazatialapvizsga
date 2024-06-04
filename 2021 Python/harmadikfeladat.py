class Versenyzok:
    def __init__(self,nev,nem,sznap,uszas,kerekpar,futas,rszam):
        self.nev = nev
        self.nem = nem
        self.sznap = sznap
        self.uszas = uszas
        self.kerekpar = kerekpar
        self.futas = futas
        self.rszam = int(rszam)

    def osszIdo(self):
        return sum([int(t.split(":")[0]) * 3600 + int(t.split(":")[1]) * 60 + int(t.split(":")[2]) for t in [self.uszas, self.kerekpar, self.futas]])
f = open("triatlon.txt","r")
next(f)

versenyzok = []
for egySor in f:
    sor = egySor.strip().split(";")
    nev, nem, sznap, uszas, kerekpar, futas, rszam = sor
    versenyzok.append(Versenyzok(nev,nem,sznap,uszas,kerekpar,futas,rszam))

f.close()
induloVersenyzo = len(versenyzok)

print("2. feladat: A versenyen "+str(induloVersenyzo)+" induló volt.")

nyertes = min(versenyzok, key=Versenyzok.osszIdo)
osszIdo = nyertes.osszIdo()
print("3. feladat: A verseny nyertese:")
print("\tneve: "+nyertes.nev)
print("\trajtszáma: "+str(nyertes.rszam))
print("\tösszideje: "+ str(osszIdo // 3600) + ":" + str(osszIdo % 3600 // 60) + ":" + str(osszIdo % 60))

f = open ("osszidok.txt","w")

for egyVersenyzo in versenyzok:
    osszIdo = egyVersenyzo.osszIdo()
    f.write(f"{egyVersenyzo.rszam};{egyVersenyzo.nev};{osszIdo // 3600};{osszIdo % 3600 // 60};{osszIdo % 60}\n")