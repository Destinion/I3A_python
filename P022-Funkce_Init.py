#Funkce init
#Vytvoří nový objekt a vrátí ho
#Praktická funkce pro vytvoření nového objektu
#Bez použití funkce init bychom museli vytvořit nový objekt a pak všechny jeho atributy
#Použití funkce init je jednodušší a přehlednější
#Funkce init je volána automaticky při vytvoření nového objektu

class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        
osoba1 = Osoba("Petr", 25)

print(osoba1.jmeno)
print(osoba1.vek)