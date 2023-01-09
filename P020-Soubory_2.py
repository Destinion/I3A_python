#Práce se soubory v pythonu - 2. část

#Základním příkazem pro práci se soubory je open()
#open() má 2 povinné parametry - jméno souboru a režim otevření

open("soubor.txt", "r") #otevře soubor soubor.txt v režimu čtení
open("soubor.txt", "w") #otevře soubor soubor.txt v režimu zápisu
open("soubor.txt", "a") #otevře soubor soubor.txt v režimu přidávání
open("soubor.txt", "r+") #otevře soubor soubor.txt v režimu čtení a zápisu
open("soubor.txt", "w+") #otevře soubor soubor.txt v režimu čtení a zápisu
open("soubor.txt", "a+") #otevře soubor soubor.txt v režimu čtení a přidávání

#Výchozí režim je "r" - čtení
#-------------------------------------------------------------
open("ukazka.txt")
print(open("ukazka.txt").read()) #vypíše obsah souboru ukazka.txt

#Vypsání pouze prvních 5 znaků
print(open("ukazka.txt").read(5))

#Vypsání obsahu souboru po řádcích
print(open("ukazka.txt").readlines())

#Vypsání obsahu souboru po řádcích do seznamu
for line in open("ukazka.txt").readlines():
    print(line)
    
#Psaní do souboru
f = open("ukazka2.txt", "w") #otevření souboru v režimu zápisu
f.write("Toto je ukazka zapisu do souboru") #zapsání textu do souboru
print(open("ukazka2.txt").read()) #vypsání obsahu souboru
f.close() #zavření souboru




    

