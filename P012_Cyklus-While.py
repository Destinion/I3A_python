#Cyklus While
#Slouží pro cyklické opakování až do splnění podmínky

#Vytvoříme si proměnnou a přiřadíme jí hodnotu 0
i = 0

#Začneme cyklus While
#V podmínce je i menší než 10
while i < 10:
    #Vypíšeme hodnotu proměnné i
    print(i)
    #Přičteme k proměnné i hodnotu 1
    i = i + 1

#Break
#Přeruší cyklus

j = 0
while j < 10:
    print(j)
    if j == 5:
        break
    j = j + 1

#Continue
#Přeskočí cyklus

k = 0
while k < 10:
    k = k + 1
    if k == 5:
        continue
    print(k)

#else
# Vykona se po ukončení cyklu
# V případě použití break se else neprovede
# V případě použití continue se else provede

l = 0
while l < 10:
    print(l)
    l = l + 1
else:
    print("Cyklus byl dokončen")
        





