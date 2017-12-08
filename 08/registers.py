registers = dict()
max_value = 0

def create_register_if_not_exists(register):
    if register not in registers:
        registers[register] = 0

def modify_register(inst):
    global max_value
    create_register_if_not_exists(inst[0])
    if inst[1] == 'inc':
        registers[inst[0]] += int(inst[2])
    else:
        registers[inst[0]] -= int(inst[2])
    if registers[inst[0]] > max_value:
        max_value = registers[inst[0]]

def eval_register(inst):
    create_register_if_not_exists(inst[0])
    inst[0] = "registers['"+inst[0]+"']"
    return eval(" ".join(inst))

with open("input.txt") as f:
    for rows in f:
        instruction = rows.split()
        if eval_register(instruction[4:]):
            modify_register(instruction[:3])

print(max(registers.values()))
print(max_value)
