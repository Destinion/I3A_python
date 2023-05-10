import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="praxes1677454318", heslo="heslododb", database="praxes1677454318")

#deklarace kurzoru pro komunikaci s db
deklarace = mydb.cursor()

#zobrazení db - pokud existují
deklarace.execute("SHOW DATABASES")
#vypsání db do konzole
for i in deklarace:
    print(i)

#vytvoření databáze
deklarace.execute("CREATE DATABASE databaze1")

#vytvoření tabulky
deklarace.execute("CREATE TABLE Tzakaznik(ID INT PRIMARY KEY, jmeno VARCHAR(50), prijmeni VARCHAR(60), cena_nakupu FLOAT(53))") #FLOAT - pokud je hodnota v rozpětí 0-24 tak je to FLOAT; od 25-53 je to DOUBLE

#zobrazení tabulek
deklarace.execute("SHOW TABLES")
for i in deklarace:
    print(i)
    
#vložení dat do tabulky
mydb = "INSERT INTO Tzakaznik (ID, jmeno, prijmeni, cena_nakupu) VALUES (1, 'Martin', 'Štefl', 650)"

#druhý typ vložení dat do tabulky
mydb = "INSERT INTO Tzakaznik (ID, jmeno, prijmeni, cena_nakupu) VALUES (%i, %s, %s, %f)"
uzivatel = (2, 'Karel', 'Martirosjan', 800)
deklarace.execute (mydb, uzivatel)

#uložení do tabulky
deklarace.commit()

#vložení uživatele pomocí python - user input
print("Zadej uživatele do tabulky Tzakaznik")

jmeno = input("zadej jméno: ")
prijmeni = input("zadej příjmení: ")
float(cena_nakupu) = input("zadej cenu nákupu: ")


uzivatel = (, jmeno, prijmeni, cena_nakupu)
deklarace.execute(mydb, uzivatel)

for i in range(10):
    print("Zadej uživatele do tabulky Tzakaznik")

    jmeno = input("zadej jméno: ")
    prijmeni = input("zadej příjmení: ")
    cena_nakupu = input("zadej cenu nákupu: ")

    ID = deklarace.rowcount() + 1 #deklaruje ID jako počet řádku v TB+1
    uzivatel = (ID, jmeno, prijmeni, cena_nakupu)
    deklarace.execute(mydb, uzivatel)
    deklarace.commit() #provede změny do tabulky
    i+=1


#Výpis tabulky
deklarace.execute("SELECT * FROM Tzakaznik")

#získání výsledků
vystup = deklarace.fetchall()

for i in vystup:
    print(i)





