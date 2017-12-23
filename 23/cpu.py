register_list = "abcdefgh"
registers = dict()
for x in register_list:
    registers[x] = 0

instructions = list()


def get_int(regs, argument):
    if argument.isalpha():
        return regs[argument]
    return int(argument)


with open("input1.txt") as f:
    for instruction in f:
        instructions.append(instruction)

pointer = 0
multiplications = 0

while pointer < len(instructions):
    instruction = instructions[pointer]
    command = instruction.split()[0]
    arg1 = instruction.split()[1]
    arg2 = instruction.split()[2]
    if command == "set":
            registers[arg1] = get_int(registers, arg2)
    if command == "sub":
            registers[arg1] -= get_int(registers, arg2)
    if command == "mul":
            registers[arg1] *= get_int(registers, arg2)
            multiplications += 1
    if command == "jnz":
        if get_int(registers, arg1) != 0:
                pointer += get_int(registers, arg2)
                continue
    pointer += 1

print(multiplications)