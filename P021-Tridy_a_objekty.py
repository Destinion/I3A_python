#Třídy a objekty
#Třída je návrhový vzor, který definuje vlastnosti a chování objektu.
#Objekt je instance třídy, která má vlastní vlastnosti a chování.
#Třída je definována pomocí klíčového slova class.
#Objekt je vytvořen pomocí konstruktoru třídy. - Konstruktor je metoda, která je volána při vytváření objektu.

class Auto: #Třída Auto
    def __init__(self, spz, barva): #Konstruktor třídy Auto
        self.spz = spz #Vlastnost spz
        self.barva = barva #Vlastnost barva
 
    def vypis_info(self): #Metoda vypis_info
        print("SPZ: ", self.spz) 
        print("Barva: ", self.barva)
        
auto1 = Auto ("4A2 3020", "červená") #Vytvoření objektu auto1



