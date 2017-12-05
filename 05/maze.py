# part 1

with open("input1.txt") as f:
    maze = [int(x) for x in f]

i = 0
count = 0

while True:
    if i < 0 or i >= len(maze):
        print(count)
        break
    move = maze[i]
    maze[i] += 1
    count += 1
    i += move


# part 2

with open("input1.txt") as f:
    maze = [int(x) for x in f]

i = 0
count = 0

while True:
    if i < 0 or i >= len(maze):
        print(count)
        break
    move = maze[i]
    if move > 2:
        maze[i] -= 1
    else:
        maze[i] += 1
    count += 1
    i += move
