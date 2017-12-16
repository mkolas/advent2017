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

dancers = [x for x in 'abcdefghijklmnop']

with open("input1.txt") as f:
    line = f.readline()
    moves = [x for x in line.split(',')]

for x in range(1):
    print("On iteration {}", x)
    for move in moves:
        if 's' in move:
            dancers = spin(dancers, int(''.join(move[1:])))
            continue
        arg1 = move[1:].split('/')[0]
        arg2 = move[1:].split('/')[1]
        if 'x' in move:
            dancers = exchange(dancers, int(arg1), int(arg2))
        if 'p' in move:
            dancers = partner(dancers, arg1, arg2)

print(''.join(dancers))