f = open("DFA1")
g = open("DFA2")

trap_state = "trap"

d1 = {}
n = int(f.readline())    #nr stari
S1 = []          #starile
for stare in f.readline().split():
    S1.append(int(stare))
for x in S1:
    if x not in d1:
        d1[x] = []               #dictionar cu tranzitii
l = int(f.readline())           #numar de litere
L = []                          #litere
for litera in f.readline().split():
    L.append(litera)
stare_init1 = int(f.readline())          #stare initiala
sf = int(f.readline())                  #numar stari finale
SF1 = []                                 #stari finala
for stare in f.readline().split():
    SF1.append(int(stare))
d = {}
tranzitii = int(f.readline())           #nr tranzitii
for i in range(tranzitii):
    aux = f.readline().split()
    daux = {aux[1]: int(aux[2])}
    d1[int(aux[0])].append(daux)   #introduc tranzitiile in dictionar pt DFA1


for cheie in d1:
    for litera in L:
        ok = 0
        for dictionar in d1[cheie]:
            if litera in dictionar:
                ok = 1
        if ok == 0:
            d1[cheie].append({litera: trap_state})
d1[trap_state] = []
for litera in L:
    d1[trap_state].append({litera: trap_state})
S1.append(trap_state)
print(S1)
print(d1)


d2 = {}
n = int(g.readline())    #nr stari
S2 = []          #starile
for stare in g.readline().split():
    S2.append(int(stare))
for x in S2:
    if x not in d2:
        d2[x] = []               #dictionar cu tranzitii
l = int(g.readline())           #numar de litere
L = []                          #litere
for litera in g.readline().split():
    L.append(litera)
stare_init2 = int(g.readline())          #stare initiala
sf2 = int(g.readline())                  #numar stari finale
SF2 = []                                 #stari finala
for stare in g.readline().split():
    SF2.append(int(stare))
tranzitii = int(g.readline())           #nr tranzitii
for i in range(tranzitii):
    aux = g.readline().split()
    daux = {aux[1]: int(aux[2])}
    d2[int(aux[0])].append(daux)   #introduc tranzitiile in dictionar pt DFA2
for cheie in d2:
    for litera in L:
        ok = 0
        for dictionar in d2[cheie]:
            if litera in dictionar:
                ok = 1
        if ok == 0:
            d2[cheie].append({litera: trap_state})
d2[trap_state] = []
for litera in L:
    d2[trap_state].append({litera: trap_state})
S2.append(trap_state)
print(S2)
print(d2)

# Complement DFA1
CSF1 = []                  #stari finale complement 1
for stare in S1:
    if stare not in SF1 and stare != trap_state:
        CSF1.append(stare)

# Complement DFA2
CSF2 = []                  #stari finale complement 2
for stare in S2:
    if stare not in SF2 and stare != trap_state:
        CSF2.append(stare)

#Intersectia DFA1 cu Complement DFA2 (daca intersectia este nula, inseamna ca DFA1 inclus in DFA2)
SI = []
SFI1 = []
I = {}
for cheie1 in d1:
    for cheie2 in d2:
        SI.append((cheie1, cheie2))
        if cheie1 in SF1 and cheie2 in CSF2:
            SFI1.append((cheie1,cheie2))
#print(SI)
#print(SFI1)
stare_init_intersectie = (stare_init1, stare_init2)
for stare in SI:
    I[stare] = []
    for litera in L:
        for dictionar in d1[stare[0]]:
            if litera in dictionar:
                s1 = dictionar[litera]
        for dictionar in d2[stare[1]]:
            if litera in dictionar:
                s2 = dictionar[litera]
        I[stare].append({litera: (s1,s2)})
print(I)

vizitat = set()
queue = [stare_init_intersectie]
ok1 = 1
while queue:
    stare_curenta = queue.pop(0)
    if stare_curenta in vizitat:
        continue
    vizitat.add(stare_curenta)
    if stare_curenta in SFI1:
        break
    for litera in L:
        for dictionar in I[stare_curenta]:
            if litera in dictionar:
                urm_stare = dictionar[litera]
        if urm_stare not in vizitat:
            queue.append(urm_stare)
else:
    ok1 = 0
print(ok1)

#Ok = 0 inseamna ca intersectia e nula pentru ca face verificari pana se termina natural whileul (adica nu gaseste nicio stare finala plecand din starea initiala)

#Intersectia DFA2 cu Complement DFA1 (daca intersectia este nula, inseamna ca DFA2 inclus in DFA1)
SFI2 = []
for cheie1 in d1:
    for cheie2 in d2:
        if cheie1 in CSF1 and cheie2 in SF2:
            SFI1.append((cheie1,cheie2))

vizitat = set()
queue = [stare_init_intersectie]
ok2 = 1
while queue:
    stare_curenta = queue.pop(0)
    if stare_curenta in vizitat:
        continue
    vizitat.add(stare_curenta)
    if stare_curenta in SFI1:
        break
    for litera in L:
        for dictionar in I[stare_curenta]:
            if litera in dictionar:
                urm_stare = dictionar[litera]
        if urm_stare not in vizitat:
            queue.append(urm_stare)
else:
    ok2 = 0

print(ok2)

if ok1 == 0 and ok2 == 0:
    print("Sunt echivalente")
else:
    print("Nu sunt echivalente")