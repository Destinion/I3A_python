print("Typy proměnných - hlavní typy")
print("")

print("1. Celá čísla (int)")
int1 = 1 # celé číslo
int2 = int(2)

print( "2. Desetinná čísla (float)")
float1 = 1.0   # desetinná čísla se zapisují s tečkou
float2 = float(2.0)

print("3. Řetězce (str)")
str1 = "Ahoj" # řetězec

print("4. Logické hodnoty (bool)")
bool1 = True # logická hodnota
bool2 = False

print("5. None")
none1 = None # None

print("6. Seznamy (list)")
list1 = [1, 2, 3] # seznam
list2 = list([1, 2, 3])

print("7. Komplexní číla (complex)")
complex1 = 1j # komplexní číslo
complex2 = complex(2j)

print("8. Slovníky (dict)")
dict1 = {"a": 1, "b": 2, "c": 3} # slovník
dict2 = dict({"a": 1, "b": 2, "c": 3})

print("9. Množiny (set)")
set1 = {1, 2, 3} # množina
set2 = set([1, 2, 3])

print("10. Tropy (tuple)")
tuple1 = (1, 2, 3) # tuple
tuple2 = tuple([1, 2, 3])

print("11. Byty (bytes)")
bytes1 = b"Hello" # bytes
bytes2 = bytes(5)

print("12. Byty (bytearray)")
bytearray1 = bytearray(5) # bytearray
bytearray2 = bytearray(5)

print("13. Příkaz range")
range1 = range(6) # range

print("14. Příkaz enumerate")
enumerate1 = enumerate(["a", "b", "c"]) # enumerate

print("15. Příkaz filter")
filter1 = filter(None, [1, 0, False, True]) # filter

print("16. Příkaz map")
map1 = map(lambda x: x*x, [1, 2, 3, 4, 5]) # map

print("17. Příkaz zip")
zip1 = zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) # zip

print("18. Příkaz frozenset")
frozenset1 = frozenset([1, 2, 3, 4, 5]) # frozenset

print("19. Příkaz memoryview")
memoryview1 = memoryview(bytes(5)) # memoryview

print("20. Příkaz object")
object1 = object() # object

print("21. Příkaz slice")
slice1 = slice(1, 5, 2) # slice


print("Proměnné lze měnit i pouze pro výstup pomocí typ(proměnná)")
