played = 0
register_list = "iapbf"
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

while True:
    instruction = instructions[pointer]
    command = instruction.split()[0]
    print(command)
    arg1 = instruction.split()[1]
    if command == "snd":
        played = registers[arg1]
        pointer += 1
        continue
    if command == "rcv":
        if registers[arg1] > 0:
            print("recovered {}".format(played))
            break
        pointer += 1
        continue
    arg2 = instruction.split()[2]
    if command == "set":
            registers[arg1] = get_int(registers, arg2)
    if command == "add":
            registers[arg1] += get_int(registers, arg2)
    if command == "mul":
            registers[arg1] *= get_int(registers, arg2)
    if command == "mod":
            registers[arg1] %= get_int(registers, arg2)
    if command == "jgz":
        if get_int(registers, arg1) > 0:
                pointer += get_int(registers, arg2)
                continue
    pointer += 1

