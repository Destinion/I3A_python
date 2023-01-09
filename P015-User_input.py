#User input pomocí pythonu

#Vstupní proměnná
name = input("Zadej jméno: ")

#Výstup
print("Ahoj " + name)

#Program se ukončí až po stisknutí klávesy
input("Stiskni libovolnou klávesu pro ukončení programu...")

#Praktické ukázky
#Výpočet věku
age = input("Zadej svůj věk: ")
print("Věk je: " + age)

#Výpočet věku za 10 let
age = input("Zadej svůj věk: ")
print("Věk za 10 let bude: " + str(int(age) + 10))

#Zadání čísla a výpočet jeho druhé mocniny
number = input("Zadej číslo: ")
print("Druhá mocnina čísla je: " + str(int(number) ** 2))

#Zadání hodnot do seznamu
list = []
for i in range(3):
    list.append(input("Zadej hodnotu: "))
print(list)
