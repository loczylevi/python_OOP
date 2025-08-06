# python_OOP
## https://sulipy.hu/oop/osztaly_objektum?tab=video
```python
import random

"""A kör területe a sugár négyzetének és a π-nek a szorzata"""

import math
class Kor:  #terv rajz
    def __init__(self, sugar=0,kozeppont=(0,0)): # ez a függvény arrol tanuskodik hpgy ez a class alapján hozzon létre példányokat
        self.sugar = sugar
        self.kozeppont = kozeppont
        
    def terulet(self):
        return (self.sugar**2) * math.pi
    
    def kerulet(self):
        return (self.sugar*2) * math.pi

kor01 = Kor(5, (4,7)) # maga a ház objektum

print(kor01)
print(type(kor01))
print(isinstance(kor01, Kor)) # ez class valóban ehez objektumhoz tartozik
print(kor01.kozeppont)
print(kor01.terulet())
print(kor01.kerulet())

kor02 = Kor(10, (1,1))   # ezek objektumok
print("\n__________________________________________________________\n")

print(kor02)
print(type(kor02))
print(isinstance(kor02, Kor)) # ez class valóban ehez objektumhoz tartozik
print(kor02.kozeppont)
print(kor02.terulet())
print(kor02.kerulet())


lista = []

for szam in range(100):
    radius = random.randint(0,100)
    x = random.randint(0,100)
    y = random.randint(0,100)
    ciklus_kor = Kor(radius, (x,y))
    lista.append(ciklus_kor)
    

for sor in lista:
    print(f"radius: {sor.sugar} kordinata:\nx: {sor.kozeppont[0]} y: {sor.kozeppont[1]}\n terület: {sor.terulet()} kerület: {sor.kerulet()}")



```
