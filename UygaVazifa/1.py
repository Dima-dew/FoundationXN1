import os
os.system("cls")

f = open("n1.txt", "r")
son = f.read()
f.close()

f1 = open("n2.txt", "r")
son1 = f1.read()
f1.close()

natija = son.split("\n")
natija2 = son1.split("\n")

f2 = open("davlatlar.txt", "w")
katta = max(len(natija), len(natija2))

for i in range(katta):
    ciq = natija[i]
    if i < len(natija):
        chiq = natija2[i]
    if i < len(natija2):
        f2.write(f"{ciq} -{chiq}\n")