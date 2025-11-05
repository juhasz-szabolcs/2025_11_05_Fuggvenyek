"""
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, 
ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, 
és a képernyőre kiírja, melyik a legrövidebb szó!
"""
szavak = []

# szo1 = input("Kérlek add meg az 1. szót! ")
# szo2 = input("Kérlek add meg az 2. szót! ")
# szo3 = input("Kérlek add meg az 3. szót! ")

# szavak.append(szo1)
# szavak.append(szo2)
# szavak.append(szo3)

def legrovidebb_szo_kereso(szavak_listaja):
    legrovidebb = len(szavak_listaja[0])
    legrovidebb_szo = szavak_listaja[0]

    for szo in szavak_listaja:
        if len(szo) < legrovidebb:
            legrovidebb = len(szo)
            legrovidebb_szo = szo
    
    print(f"A legrövidebb szó: {legrovidebb_szo}. Karakterszama: {legrovidebb}")


szok = ["alma", "banán", "kivi", "sárkánygyümölcs", "dió"]
# legrovidebb_szo_kereso(szavak)
legrovidebb_szo_kereso(szok)

