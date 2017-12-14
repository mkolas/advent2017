from knot import knot_hash

input_string = "ljoxqyyw"

# part 1

square_count = 0

for x in range(128):
    knot = knot_hash(input_string+"-"+str(x))
    bin_string = bin(int(knot, 16))[2:].zfill(128)
    for y in bin_string:
        if y == '1':
            square_count += 1

print("Num of 1s: {}".format(square_count))


# part 2

def check_adjacent(y, x, grid):
    if grid[y][x].isdigit() and grid[y][x] != '0':
        return True
    else:
        return False


def check_regions(y, x, grid, size):
    to_set = 'X'
    if y != 0 and check_adjacent(y-1, x, grid):
        to_set = grid[(y-1) % size][x % size]
    elif x != size - 1 and check_adjacent(y, x+1, grid):
        to_set = grid[y % size][(x+1) % size]
    elif y != size - 1 and check_adjacent(y+1, x, grid):
        to_set = grid[(y+1) % size][x % size]
    elif x != 0 and check_adjacent(y, x-1, grid):
        to_set = grid[y % size][(x-1) % size]
    return to_set


def replace_all_in_grid(grid, old, new):
    for y in range(len(disk_grid)):
        for x in range(len(disk_grid[y])):
            if grid[y][x] == old:
                grid[y][x] = new


region_count = 0
disk_grid = list()

for x in range(128):
    knot = knot_hash(input_string+"-"+str(x))
    bin_string = bin(int(knot, 16))[2:].zfill(128)
    bin_string = bin_string.replace("1", "X")
    disk_grid.append(list(bin_string))

# first, check backwards
for y in range(len(disk_grid)):
    for x in range(len(disk_grid[y])):
        if disk_grid[y][x] == 'X':
            region = check_regions(y, x, disk_grid, 128)
            if region == 'X':
                region_count += 1
                disk_grid[y][x] = str(region_count)
            else:
                disk_grid[y][x] = region

# then reduce
for y in range(len(disk_grid)):
    for x in range(len(disk_grid[y])):
        if disk_grid[y][x] != '0':
            region = check_regions(y, x, disk_grid, 128)
            if region != 'X' and int(region) != int(disk_grid[y][x]):
                region_count -= 1
                replace_all_in_grid(disk_grid, disk_grid[y][x], region)

print("Number of regions: {}".format(region_count))
