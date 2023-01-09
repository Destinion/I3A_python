#Správa chyb a výjimek
#Výjimky jsou chyby, které se vyskytují během běhu programu a které jsou nepředvídatelné. Výjimky jsou dědičné od třídy Exception.

try: #pokusí se vykonat následující kód
    x = int(input("Zadejte číslo: "))
    y = int(input("Zadejte číslo: "))
    print(x/y)
except ZeroDivisionError: #pokud dojde k chybě typu ZeroDivisionError, tak se vykoná následující kód
    print("Nulou nelze dělit!")
except ValueError: #pokud dojde k chybě typu ValueError, tak se vykoná následující kód
    print("Musíte zadat číslo!")
except: #pokud dojde k chybě jiného typu, tak se vykoná následující kód
    print("Nastala chyba!")
else: #pokud se nepodaří vykonat žádný z bloků except, tak se vykoná následující kód
    print("Vše v pořádku!")
finally: #tento blok se vždy vykoná
    print("Toto se vždy vykoná!")

