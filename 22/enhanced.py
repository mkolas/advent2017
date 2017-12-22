grid = dict()
infections = 0
direction = (0, -1)
position = (12, 12)


def add(t1, t2):
    return t1[0]+t2[0], t1[1]+t2[1]


def turn_right(direct):
    if direct == (1, 0):
        return 0, 1
    if direct == (0, 1):
        return -1, 0
    if direct == (-1, 0):
        return 0, -1
    if direct == (0, -1):
        return 1, 0


def turn_left(direct):  # i cant turn left pops
    return turn_right(turn_right(turn_right(direct)))


def turn_around(direct):
    if direct == (1, 0):
        return -1, 0
    if direct == (0, 1):
        return 0, -1
    if direct == (-1, 0):
        return 1, 0
    if direct == (0, -1):
        return 0, 1


def create_if_not_exists(pos):
    if pos not in grid:
        grid[pos] = '.'


with open("input1.txt") as f:
    for y, row in enumerate(f):
        row_list = list()
        for x, c in enumerate(row.strip()):
                grid[(x, y)] = c


for x in range(10000000):
    if grid[position] is '.':
        direction = turn_left(direction)
        grid[position] = 'W'
    elif grid[position] is 'W':
        grid[position] = '#'
        infections += 1
    elif grid[position] is 'F':
        direction = turn_around(direction)
        grid[position] = '.'
    elif grid[position] is "#":
        direction = turn_right(direction)
        grid[position] = 'F'
    position = add(position, direction)
    create_if_not_exists(position)

print("Number of bursts causing infections: ", infections)

