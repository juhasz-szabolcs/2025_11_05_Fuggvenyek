"""
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, 
és a képernyőre kiírja, melyik a nagyobb szám!
Kezeld azt az esetet is, ha a két szám egyenlő!
"""

def ket_szam_osszehasonlitasa(x, y):
    if x > y:
        print(f"Az első szám nagyobb, értéke {x}")
    elif x < y:
        print(f"A második szám nagyobb, értéke {y}")
    else:
        print("A két szám egyenlő")

szam1 = int(input("Kérlek adj meg egy számot! "))
szam2 = int(input("Kérlek adj meg egy számot! "))
ket_szam_osszehasonlitasa(szam1, szam2)
