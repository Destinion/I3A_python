#Dědičnost v Pythonu - inheritance

#Dědičnost je v Pythonu velmi jednoduchá. Vytvoříme si třídu, která bude dědit od jiné třídy.
#Dědičnost nám dovolí vytvořit novou třídu, která bude mít všechny vlastnosti a metody původní třídy.

class Zamestnanec:
    def __init__(self, jmeno, plat):
        self.jmeno = jmeno
        self.plat = plat

    def zvys_plat(self, procenta): #Zvýšíme si plat o zadaný počet procent.
        self.plat = self.plat * (1 + procenta / 100)

    def vypis(self): #Vypíšeme si jméno a plat.
        print("Jméno: ", self.jmeno)
        print("Plat: ", self.plat)
        
x = Zamestnanec("Petr", 10000) #Vytvoříme si instanci třídy Zamestnanec.
x.vypis()

#Vytvoříme si třídu Programátor, která bude dědit od třídy Zamestnanec.
class Programator(Zamestnanec): #Závorky jsou zde proto, aby Python věděl, od které třídy bude dědit.
    def __init__(self, jmeno, plat, jazyk):
        Zamestnanec.__init__(self, jmeno, plat)
        self.jazyk = jazyk

    def vypis(self):
        Zamestnanec.vypis(self)
        print("Jazyk: ", self.jazyk)
        
y = Programator("Petr", 10000, "Python") #Vytvoříme si instanci třídy Programátor.
y.vypis()
