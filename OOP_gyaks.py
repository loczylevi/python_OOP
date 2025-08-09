"""1.1 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály.
Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület
és terület számításra is egy-egy metódussal!
"""


"""
=======PUSKA========
Analógia:
Ha lenne egy Auto osztály:

szin, sebesseg, marka → ezek attribútumok

indit(), fekez() → ezek metódusok (az objektum viselkedését leíró függvények)

==============================
"""

class Negyzet:
    def __init__(self, oldal_hossz = 0):
        self.oldal_hossz = oldal_hossz
    
    def terulet(self):
        return self.oldal_hossz ** 2
    
    def kerulet(self):
        return self.oldal_hossz * 4
    
    def atlo(self):
        return (2 ** 0.5) * self.oldal_hossz
    
    def __add__(self, other): # operátor túlterhelés mert miért ne ༼ つ ◕_◕ ༽つ
        if isinstance(other, Negyzet):
            return Negyzet(self.oldal_hossz + other.oldal_hossz)
        
    def __ge__(self, other): # operátor túlterhelés mert miért ne ༼ つ ◕_◕ ༽つ
        if isinstance(other, Negyzet):
            return self.oldal_hossz >= other.oldal_hossz
        
    def __eq__(self, other): # operátor túlterhelés mert miért ne ༼ つ ◕_◕ ༽つ
        if isinstance(other, Negyzet):
            return self.oldal_hossz == other.oldal_hossz
    
    def __str__(self):
        return (f"Negyzet: oldal = {self.oldal_hossz}, "
                f"kerület = {self.kerulet()}, "
                f"terület = {self.terulet()}, "
                f"átló = {self.atlo():.2f}")
    
    
    
    
negyzset1 = Negyzet(4)
negyzset2 = Negyzet(6)

osszead = negyzset1 + negyzset2

print(negyzset1.oldal_hossz)
print(negyzset1.terulet())
print(negyzset1.kerulet())
print(negyzset1.atlo())

print(negyzset1)

print(osszead.oldal_hossz)


"""
1.2 Feladat
Módosítsd az előző programot úgy, hogy a metódus ne a kerület- illetve a területértékkel térjen vissza,
hanem maga gondoskodjon ezen értékek kiírásáról egy egész mondatos formában.
"""


class Negyzet2:
    def __init__(self, oldal_hossz = 0):
        self.oldal_hossz = oldal_hossz
    
    def terulet(self):
        return f"A négyzet területe: {self.oldal_hossz ** 2}\t༼ つ ◕_◕ ༽つ"
    
    def kerulet(self):
        return f"A négyzet kerülete: {self.oldal_hossz * 4}\t༼ つ ◕_◕ ༽つ"
    
    def atlo(self):
        return f"A négyzet átlója {(2 ** 0.5) * self.oldal_hossz}\t༼ つ ◕_◕ ༽つ"
    

    
    
negyzset3 = Negyzet2(3)

print(negyzset3.terulet())
print(negyzset3.kerulet())
print(negyzset3.atlo())

"""1.3 Feladat
Az 1.1 feladatban meghatározottak szerint készíts egy programot,
amely a felhasználótól egymás után bekér négyzetek oldalhosszát egészen addíg,
amíg a felhasználó 0 értéket nem ad meg!
Ezen adat alapján a program hozzon létre negyzet objektumokat,
melyeket egy listában tárol!
A program írja ki a megadott négyzetek oldalhosszát, kerületét és területét!
"""
print("\n============== 1.3 Feladat ===============\n")
bekeres = int(input("Kérem a négyzet oldalhosszát: (kilépés 0): "))
lista = ["első_érték: oldal_hossz", "2. kerulet", "3. terulet", "4. atlo"]
while bekeres != 0:
    bekeres = int(input("Kérem a négyzet oldalhosszát: (kilépés 0): "))
    if bekeres == 0:
        break
    else:
        negyzset4 = Negyzet(bekeres)
        print(negyzset4)
        lista.append([negyzset4.oldal_hossz, negyzset4.kerulet(), negyzset4.terulet(), negyzset4.atlo()])
    

"""
2. Feladat
Készíts egy programot, amely objektumorientált módon tartja nyilván kutyák adatait
(név, életkor, nem)! A nevét a felhasználó adja meg, az életkorát és a nemét véletlenszerűen
határozza meg a program! Befejezésként a program a képernyőre írja ki a megadott kutyák adatait!
"""
    
    
