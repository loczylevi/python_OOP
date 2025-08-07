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



    
    
    
    
