#Výběr náhodného čísla z intervalu <0,100>
import random
cislo = random.randint(0,100)
print("Náhodné číslo je: ", cislo)

#Hádání čísla od uživatele
#Výběr náhodného čísla z intervalu <0,100>
cislo = random.randint(0,100)
guess = int(input("Hádej číslo: "))
while guess != cislo:
    if guess < cislo:
        print("Hodnota je menší")
    else:
        print("Hodnota je větší")
    guess = int(input("Hádej číslo: "))
print("Uhádl jsi číslo: ", cislo)
