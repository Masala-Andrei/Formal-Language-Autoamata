with open("input.txt") as f:
    n = int(f.readline().strip())
    S = f.readline().strip().split()  #

    l = int(f.readline().strip())
    L = f.readline().strip().split()

    stare_initiala = f.readline().strip()

    sf = int(f.readline().strip())
    SF = f.readline().strip().split()

    nrtranz = int(f.readline().strip())
    d = {}
    for _ in range(nrtranz):
        aux = f.readline().strip().split()
        if (aux[0], aux[1], aux[2]) not in d:
            d[(aux[0], aux[1], aux[2])] = []
        d[(aux[0], aux[1], aux[2])].append((aux[3], aux[4]))

cuvant = input("Introduceti cuvantul: ")
F = []
def verificare(input_string, stare_curenta, stack):
    global d, SF,F

    simbol_curent = input_string[0] if input_string else "."
    next_input = input_string[1:] if input_string else ""
    top_stack = stack[-1]
    lista = []

    if stare_curenta in SF and not input_string and stack == ['Z']:
        F.append(1)

    if simbol_curent != ".":
        if (stare_curenta, simbol_curent, top_stack) in d:
            for tranz in d[(stare_curenta, simbol_curent, top_stack)]:
                lista.append((tranz[0], tranz[1], simbol_curent))
    if (stare_curenta, ".", top_stack) in d:
        for tranz in d[(stare_curenta, ".", top_stack)]:
            lista.append((tranz[0],tranz[1],"."))


    for (operatii_stack, urm_stare, simb) in lista:
        new_stack = stack[:-1]
        for litera in reversed(operatii_stack):
            if litera != ".":
                new_stack.append(litera)

        verificare(next_input if simb != '.' else input_string, urm_stare, new_stack)


verificare(cuvant, stare_initiala, ['Z'])
if 1 in F:
    print("Accepta cuvantul")
else:
    print("Nu accepta cuvantul")