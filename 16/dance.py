import collections

def spin(dance_array, num):
    r = collections.deque(dance_array)
    r.rotate(num)
    return list(r)

def exchange(dance_array, pos1, pos2):
    dance_array[pos1], dance_array[pos2] = dance_array[pos2], dance_array[pos1]
    return dance_array

def partner(dance_array, name1, name2):
    pos1 = dance_array.index(name1)
    pos2 = dance_array.index(name2)
    return exchange(dance_array, pos1, pos2)

def dance(dance_array, moves):
    for move in moves:
        if 's' in move:
            dance_array = spin(dance_array, int(''.join(move[1:])))
            continue
        arg1 = move[1:].split('/')[0]
        arg2 = move[1:].split('/')[1]
        if 'x' in move:
            dance_array = exchange(dance_array, int(arg1), int(arg2))
        if 'p' in move:
            dance_array = partner(dance_array, arg1, arg2)
    return dance_array

fresh_dancers = [x for x in 'abcdefghijklmnop']

with open("input1.txt") as f:
    line = f.readline()
    moves = [x for x in line.split(',')]

# part 1

dancers = fresh_dancers.copy()
dancers = dance(dancers, moves)
print(''.join(dancers))

# part 2
dancers = fresh_dancers.copy()
count = 0

while True:
    dancers = dance(dancers, moves)
    count += 1
    if ''.join(dancers) == "abcdefghijklmnop":
        print("found cycle after {} iterations".format(count))
        break

iterations_needed = 1000000000 % count

dancers = fresh_dancers.copy()
for x in range(iterations_needed):
    dancers = dance(dancers, moves)
print(''.join(dancers))