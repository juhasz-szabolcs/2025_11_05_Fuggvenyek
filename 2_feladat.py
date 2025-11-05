"""
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, 
hogy negatív, pozitív vagy nulla-e!
"""

def szam_eldontese(number):
    if number > 0:
        print("Pozitív")
    elif number < 0:
        print("Negatív")
    else:
        print("A szám 0")

szam = int(input("Kérlek adj meg egy számot! "))
szam_eldontese(szam)