from queue import Queue
from threading import Thread

# when both threads get stuck in the "waiting" state, look at the logs
# and see the last message sent by program 1

# don't know off-hand how to detect that both have halted

def performer(input_queue, output_queue, program_id):
    sent = 0
    register_list = "iapbf"
    registers = dict()
    for x in register_list:
        registers[x] = 0
    registers['p'] = program_id

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
        arg1 = instruction.split()[1]
        if command == "snd":
            output_queue.put(get_int(registers, arg1))
            sent += 1
            print("Program {} has sent {} values".format(program_id, sent))
            pointer += 1
            continue
        if command == "rcv":
            while True:
                print("Program {} waiting....".format(program_id))
                registers[arg1] = input_queue.get()
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



queue_one = Queue()
queue_two = Queue()

thread_one = Thread(target=performer, args=(queue_one, queue_two, 0,))
thread_two = Thread(target=performer, args=(queue_two, queue_one, 1,))

thread_one.start()
thread_two.start()
