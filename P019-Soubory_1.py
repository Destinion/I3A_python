#Práce se soubory v pythonu

#hlavním nástrojem pro práci se soubory je modul os
import os

#os.path.exists() - zjistí, zda soubor existuje
print(os.path.exists("C:\Python\Python37-32\Python\P19-Soubory.py"))

#os.path.isfile() - zjistí, zda se jedná o soubor
print(os.path.isfile("C:\Python\Python37-32\Python\P19-Soubory.py"))

#os.path.isdir() - zjistí, zda se jedná o adresář
print(os.path.isdir("C:\Python\Python37-32\Python\P19-Soubory.py"))

#os.path.getsize() - zjistí velikost souboru
print(os.path.getsize("C:\Python\Python37-32\Python\P19-Soubory.py"))

#os.path.getmtime() - zjistí datum poslední změny souboru
print(os.path.getmtime("C:\Python\Python37-32\Python\P19-Soubory.py"))

#os.path.getatime() - zjistí datum posledního přístupu k souboru
print(os.path.getatime("C:\Python\Python37-32\Python\P19-Soubory.py"))

#os.path.getctime() - zjistí datum vytvoření souboru
print(os.path.getctime("C:\Python\Python37-32\Python\P19-Soubory.py"))

#os.path.abspath() - zjistí absolutní cestu k souboru
print(os.path.abspath("C:\Python\Python37-32\Python\P19-Soubory.py"))

#smazání souboru - os.remove()

