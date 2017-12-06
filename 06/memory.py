from typing import List


input_ = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"

# input_ = "0 2 7 0"

blocks = [int(x) for x in input_.split()]


def max_index(memory: List[int]) -> int:
    max_ = 0  # Type: int
    index = 0  # Type: int
    for i, x in enumerate(memory):
        if x > max_:
            max_ = x
            index = i
    return index


def distribute(memory: List[int]) -> List[int]:
    target = max_index(memory)  # Type: int
    to_dist = memory[target]
    memory[target] = 0
    while to_dist > 0:
        target += 1
        memory[target % len(memory)] += 1
        to_dist -= 1
    return memory


count = 0

block_history = [(blocks[:], 0)]  # Type: List[Tuple[List[int], int]]

while True:
    distribute(blocks)
    count += 1
    if blocks not in [x[0] for x in block_history]:
        block_history.append((blocks[:], count))
    else:
        first_seen = [x[1] for x in block_history if x[0] == blocks][0]
        print("first seen: {}".format(first_seen))
        print("last seen: {}".format(count))
        print("difference: {}".format(count - first_seen))
        break
