# # #DFA
#
# f = open("input.txt")
#
# d = {}
# n = int(f.readline())    #nr stari
# S = []          #starile
# for stare in f.readline().split():
#     S.append(int(stare))
# for x in S:
#     if x not in d:
#         d[x] = []               #dictionar cu tranzitii
# l = int(f.readline())           #numar de litere
# L = []                          #litere
# for litera in f.readline().split():
#     L.append(litera)
# stare_init = int(f.readline())          #stare initiala
# sf = int(f.readline())                  #numar stari finale
# SF = []                                 #stari finala
# for stare in f.readline().split():
#     SF.append(int(stare))
# tranzitii = int(f.readline())           #nr tranzitii
# for i in range(tranzitii):
#     aux = f.readline().split()
#     d[int(aux[0])].append((aux[1],int(aux[2])))   #introduc tranzitiile in dictionar
#
# #Am citit datele
#
# def delta(cuvant,stare):
#     if cuvant == "":
#         return stare
#     else:
#         for i in range (len(d[stare])):
#             if cuvant[0] in d[stare][i]:
#                 return delta(cuvant[1:],d[stare][i][1])
#         return None
#
# for i in range (int(f.readline())):
#     x = delta(f.readline().strip(),stare_init)
#     if x == None or x not in SF:
#         print("NU")
#     else:
#         print("DA")
#
# f.close()
#
# # #NFA
#
# f = open("input.txt")
# g = open("output.txt",'w')
# d = {}
# n = int(f.readline())                     #nr stari
# S = []                                    #starile
# for stare in f.readline().split():
#     S.append(int(stare))
# for x in S:
#     if x not in d:
#         d[x] = {}                        # dictionar cu tranzitii
# l = int(f.readline())                     #numar de litere
# L = []
# for litera in f.readline().split():
#     L.append(litera)                     #literele
# stare_init = int(f.readline())          #stare initiala
# sf = int(f.readline())                  #numar stari finale
# SF = []                                 #stari finale
# for stare in f.readline().split():
#     SF.append(int(stare))
# tranzitii = int(f.readline())           #nr tranzitii
# for i in range(tranzitii):
#     aux = f.readline().split()
#     if aux[1] not in d[int(aux[0])]:
#         d[int(aux[0])][aux[1]] = [int(aux[2])]
#     else:
#         d[int(aux[0])][aux[1]].append(int(aux[2]))
#
# print(d)
# R = []
# def delta(cuvant, stare):
#     global R
#     if cuvant == "":
#         R.append(stare)
#     else:
#         if cuvant[0] in d[stare]:
#             for tranz in d[stare][cuvant[0]]:
#                  delta(cuvant[1:],tranz)
#
# for i in range(int(f.readline().strip())):
#     R = []
#     delta(f.readline().strip(),stare_init)
#     print(R)
#     for s in R:
#         if s in SF:
#             g.write("DA")
#             g.write("\n")
#             break
#     else:
#         g.write("NU")
#         g.write("\n")
# R = []
# delta("yz",stare_init)
# print(SF)
# f.close()
# g.close()

#LNFA

f = open("input.txt")
g = open("output.txt",'w')
d = {}
n = int(f.readline())    #nr stari
S = []                  #starile
for stare in f.readline().split():
    S.append(int(stare))
for x in S:
    if x not in d:
        d[x] = {}                        # dictionar cu tranzitii
l = int(f.readline())                   #numar de litere
L = []
for litera in f.readline().split():
    L.append(litera)
stare_init = int(f.readline())          #stare initiala
sf = int(f.readline())                  #numar stari finale
SF = []                                 #stari finala
for stare in f.readline().split():
    SF.append(int(stare))
tranzitii = int(f.readline())           #nr tranzitii
for i in range(tranzitii):
    aux = f.readline().split()
    if aux[1] not in d[int(aux[0])]:
        d[int(aux[0])][aux[1]] = [int(aux[2])]
    else:
        d[int(aux[0])][aux[1]].append(int(aux[2]))

R = []
V = []          #vector de vizitat
def delta(cuvant, stare):
    global R,V
    if cuvant == "":
        R.append(stare)
        if '.' in d[stare]:
            for tranz in d[stare]['.']:
                if tranz not in V:
                    V.append(tranz)
                    delta(cuvant, tranz)
    else:
        if "." in d[stare]:
            for tranz in d[stare]['.']:
                if tranz not in V:
                    V.append(tranz)
                    delta(cuvant, tranz)
        if cuvant[0] in d[stare]:
            for tranz in d[stare][cuvant[0]]:
                V.clear()
                delta(cuvant[1:],tranz)


for i in range(int(f.readline().strip())):
    R = []
    V = []
    delta(f.readline().strip(),stare_init)
    for s in R:
        if s in SF:
            g.write("DA")
            g.write("\n")
            break
    else:
        g.write("NU")
        g.write("\n")

f.close()
g.close()