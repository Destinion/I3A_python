print("Seznamy")

# Seznamy
# Seznamy jsou kolekce objektů, které jsou seřazeny podle indexu.
# Indexy začínají od 0.
# Seznamy se vytvářejí pomocí hranatých závorek.
# Seznamy jsou mutovatelné, tedy můžeme je měnit.

# Vytvoření seznamu
seznam = [1, 2, 3, 4, 5]
print(seznam)

# Přístup k prvkům seznamu
print(seznam[0])
print(seznam[1])
print(seznam[2])

#Výpis více položek
print(seznam[0:2])


# Přístup k prvkům seznamu pomocí indexu od konce
print(seznam[-1])
print(seznam[-2])
print(seznam[-3])

# Délka seznamu
print(len(seznam))

# Přidání prvku na konec seznamu
seznam.append(6)
print(seznam)

# Přidání prvku na určitou pozici
seznam.insert(0, 0)
print(seznam)

# Odstranění prvku z určité pozice
seznam.pop(0)
print(seznam)

# Přidání seznamu do seznamu
seznam.extend([7, 8, 9])
print(seznam)

# Přidání seznamu do seznamu na určitou pozici
seznam[0:0] = [0]
print(seznam)

# Cyklus procházející seznam
for i in seznam:
    print(i)

#Třídění seznamu
seznam.sort()
print(seznam)

# Odstranění prvního výskytu prvku
seznam.remove(5)
print(seznam)

# Odstranění všech výskytů prvku
seznam = [1, 2, 3, 4, 5, 5, 5, 5, 5]
seznam = [x for x in seznam if x != 5]
print(seznam)

# Shrnutí seznamu
seznam = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(sum(seznam))

# Průměr seznamu
seznam = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(sum(seznam) / len(seznam))

# Nejmenší prvek seznamu
seznam = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(min(seznam))

# Největší prvek seznamu
seznam = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(max(seznam))

# Seznamy mohou obsahovat libovolné objekty
seznam = [1, 2, 3, 4, 5, "a", "b", "c", "d", "e"]
print(seznam)