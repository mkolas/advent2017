x = 0
y = 0
max_dist = 0
with open("input1.txt") as f:
    for row in f:
        directions = [d.strip() for d in row.split(',')]
        for direction in directions:
            print(direction)
            if direction == "n":
                y += 1
            if direction == "ne":
                x += .5
                y += .5
            if direction == "se":
                x += .5
                y -= .5
            if direction == "s":
                y -= 1
            if direction == "sw":
                y -= .5
                x -= .5
            if direction == "nw":
                y += .5
                x -= .5
            if abs(x) + abs(y) > max_dist:
                max_dist = abs(x) + abs(y)

print("Steps away {}".format(abs(x) + abs(y)))
print("Furthest away {}".format(max_dist))
