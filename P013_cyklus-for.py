#cyklus for


for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

#cyklus for s podmínkou
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

#cyklus for s podmínkou a break
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
    else:
        break

#cyklus for s podmínkou a continue
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
    else:
        continue

#cyklus for s podmínkou a else
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
    else:
        print("není sudé")

#naplnění seznamu
seznam = []
for i in range(10):
    seznam.append(i)
print(seznam)

#rozbalení seznamu
seznam = [1, 2, 3, 4, 5]
for i in seznam:
    print(i)

#rozbalení seznamu s indexem
seznam = [1, 2, 3, 4, 5]
for i, j in enumerate(seznam):
    print(i, j)

#rozbalení seznamu s indexem a podmínkou
seznam = [1, 2, 3, 4, 5]
for i, j in enumerate(seznam):
    if j % 2 == 0:
        print(i, j)

#vnořené cykly
for i in range(1, 10):
    for j in range(1, 10):
        print(i, j)

#vnořené cykly s podmínkou
for i in range(1, 10):
    for j in range(1, 10):
        if i % 2 == 0 and j % 2 == 0:
            print(i, j)

#pass - přeskočí cyklus
for i in range(1, 10):
    pass

