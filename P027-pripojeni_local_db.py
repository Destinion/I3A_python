import sqlite3


#připojení db
# u serveru se zadávají přihlašovací údaje - ty lokálně nemusíme řešit

#lokální test - lokální paměť
pripojeni = sqlite3.connect(':memory:')

#povinné - nastavuje správné propojení
cursor = pripojeni.cursor()

cursor.execute('''CREATE TABLE uzivatele(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jmeno TEXT,
    prijmeni TEXT
)''')

#Ukázka dotazů SQL v pythonu
cursor.execute('''INSERT INTO uzivatele (jmeno, prijmeni) VALUES (?, ?)''', ("David", "Novák"))

#Provedení dotazu - odeslání do SQL DB
pripojeni.commit()

cursor.execute('SELECT * FROM uzivatele')
print(cursor.fetchall())


#ukončení připojení
pripojeni.close()