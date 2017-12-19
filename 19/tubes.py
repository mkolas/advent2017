tubes = dict()

position = (0, 0)
direction = (0, 1)
letters = list()
previous = "|"
steps = 0


def add(t1, t2):
    return t1[0]+t2[0], t1[1]+t2[1]


def check_lr(check):
    left = add(check, (-1, 0))
    right = add(check, (1, 0))
    if left in tubes and (tubes[left] is '-' or tubes[left].isalpha()):
        return -1, 0
    if right in tubes and (tubes[right] is '-' or tubes[right].isalpha()):
        return 1, 0


def check_ud(check):
    up = add(check, (0, -1))
    down = add(check, (0, 1))
    if up in tubes and (tubes[up] is '|' or tubes[up].isalpha()):
        return 0, -1
    if down in tubes and (tubes[down] is '|' or tubes[down].isalpha()):
        return 0, 1


with open("input1.txt") as f:
    for y, row in enumerate(f):
        row_list = list()
        for x, c in enumerate(row):
            tubes[(x, y)] = c
            if c is "|" and y == 0:
                position = (x, y)

while True:
    steps += 1
    c = tubes[position]
    if c.isalpha():
        letters.append(c)
        position = add(position, direction)
        continue
    if c is '|':
        position = add(position, direction)
        previous = c
        continue
    if c is '-':
        position = add(position, direction)
        previous = c
        continue
    if c is '+':
        if previous is '|':  # find a -
            direction = check_lr(position)
            previous = '-'
        elif previous is '-':
            direction = check_ud(position)
            previous = '|'
        position = add(position, direction)
        continue
    if c is ' ' or c is None or c is "\n":
        break

print(''.join(letters))
print(steps-1)
