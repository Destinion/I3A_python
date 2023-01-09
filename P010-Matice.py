#Matice - Tuples
# Jsou jedním ze základních datových typů v Pythonu
# Jsou to neupravitelné seznamy
# Vytvoříme je pomocí závorek
# Všechny prvky musí být stejného typu
# Prvky jsou indexovány od 0
# Prvky jsou odděleny čárkou
# Prvky mohou být jakéhokoliv typu
# Prvky mohou být i jiné matice
# Matice mohou být i vnořené

# Vytvoříme prázdnou matici
prazdna = ()
print(prazdna)

# Vytvoříme matici s jedním prvkem
jeden = (1,)
print(jeden)

# Vytvoříme matici s několika prvky
mocniny = (1, 4, 9, 16, 25)
print(mocniny)

# Vytvoříme matici s různými typy prvků
mista = ('Praha', 'Brno', 'Ostrava', 'Plzeň', 'Liberec')
print(mista)

# Vytvoříme matici s různými typy prvků
mista = ('Praha', 'Brno', 'Ostrava', 'Plzeň', 'Liberec')
print(mista)

# Vytvoříme matici s různými typy prvků
mista = ('Praha', 'Brno', 'Ostrava', 'Plzeň', 'Liberec')
print(mista)

# Výpis prvku matice
print(mista[0])
print(mista[1])

# Výpis posledního prvku matice
print(mista[-1])

#Výpis rozsahu matice
print(mista[1:3])

#Kontrola existence obsahu matice
if 'Praha' in mista:
    print('Praha je v seznamu měst')

#Výpis délky matice
print(len(mista))

#Výpis matice v cyklu
for mesto in mista:
    print(mesto)

#Spojení matic
mista2 = ('Olomouc', 'Zlín', 'Hradec Králové')
mista3 = mista + mista2
print(mista3)


