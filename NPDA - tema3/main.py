f = open ("input.txt")

n = int(f.readline())
S = []
for stare in f.readline().split():
    S.append(int(stare))

l = int(f.readline())
L = []
for litera in f.readline().split():
    L.append(litera)
stare_initiala = int(f.readline())
sf = int(f.readline())
SF = []
for stari in f.readline():
    SF.append(int(stare))
nrtranz = int(f.readline())
d = {}
for i in range(nrtranz):
    aux = f.readline().split()
    if ((aux[0],aux[1],aux[2]) not in d):
        d[(aux[0],aux[1],aux[2])] = []
    if((aux[3],aux[4]) not in d[(aux[0],aux[1],aux[2])]):
        d[(aux[0], aux[1], aux[2])].append((aux[3],aux[4]))
print(d)
cuvant = input("Introduceti cuvantul: ")


def _process(input_string, current_state, stack):
    global d, SF
    if current_state in SF and not input_string:
        return True

    current_symbol = input_string[0] if input_string else '.'
    next_input = input_string[1:] if input_string else ''
    top_stack_symbol = stack[-1] if stack else ''

    transitions_list = []

    # Collect all possible transitions
    if (str(current_state), current_symbol, top_stack_symbol) in d:
        transitions_list.extend(d[(str(current_state), current_symbol, top_stack_symbol)])
    if (str(current_state), '.', top_stack_symbol) in d:
        transitions_list.extend(d[(str(current_state), '.', top_stack_symbol)])
    print(transitions_list)
    for (stack_operations, next_state) in transitions_list:
        stack = stack[:-1] if stack else stack
        for litera in (reversed(stack_operations)):
            if litera != ".":
                stack.extend(litera)
        print(stack)
        if _process(next_input, next_state, stack):
            return True

    return False


print(_process(cuvant,stare_initiala,['z']))