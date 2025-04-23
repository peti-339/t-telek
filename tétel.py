#Programozási tételek:
#1. Maximumkiválasztás
#2. Minimumkiválasztás
#3. Összegzés
#4. Megszámolás
# A vizsgálandó lista elemei:
lista = [339, 63, 231, 840, 315, 985, 752, 986, 880, 218, 97, 403, 669, 94, 67, 199, 819, 813, 662, 445, 242, 625, 537, 892, 390, 348, 484, 862, 620, 227]
# 1. Maximumkiválasztás tétele
# A lista első elemét tekintjük kezdeti maximum értéknek
max_ertek = lista[0]
# Végigmegyünk a lista többi elemén
for i in range(1, len(lista)):
    if lista[i] > max_ertek:
        max_ertek = lista[i]
# Eredmény kiírása
print("A legnagyobb érték:", max_ertek)
# 2. Minimumkiválasztás tétele
# A lista első elemét tekintjük kezdeti minimum értéknek
min_ertek = lista[0]
# Végigmegyünk a lista többi elemén
for i in range(1, len(lista)):
    if lista[i] < min_ertek:
        min_ertek = lista[i]
# Eredmény kiírása
print("A legkisebb érték:", min_ertek)
# 3. Összegzés tétele
# Létrehozunk egy változót, amelybe folyamatosan összegezzük az elemeket
osszeg = 0
for szam in lista:
    osszeg += szam  # hozzáadjuk az aktuális elemet
# Eredmény kiírása
print("A lista elemeinek összege:", osszeg)
# 4. Megszámolás tétele
# Megszámoljuk, hogy hány elem nagyobb 541-nél
db = 0
for szam in lista:
    if szam > 541:
        db += 1  # ha nagyobb 541-nél, növeljük a számlálót
# Eredmény kiírása
print("541-nál nagyobb számok száma:", db)