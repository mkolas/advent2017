from itertools import cycle


def oscillate(iterable):
    # cycle('ABCD') --> A B C D C B A B C D ...
    reverse = False
    first = iterable[0]
    last = iterable[len(iterable)-1]
    iterator = cycle(iterable)
    reverse_iterator = cycle(iterable[::-1])
    while True:
        if reverse:
            to_return = next(reverse_iterator)
            if to_return == first:
                reverse = False
                next(iterator)
            yield to_return
            continue
        if not reverse:
            to_return = next(iterator)
            if to_return == last:
                reverse = True
                next(reverse_iterator)
            yield to_return
            continue


wall = dict()
nodes = dict()
time = 0
found = False
with open("input1.txt") as f:
    for row in f:
        depth = int(row.split(":")[0])
        size = int(row.split(":")[1])
        wall[depth] = dict(size=size, current=0, iter=oscillate(range(size)))
        next(wall[depth]["iter"])


while not found:
    # print("Checking time {}".format(time))
    # for each node, move forward
    for k in nodes:
        nodes[k] += 1

    # create node at position 0
    nodes[time] = 0

    # check if caught, add to naughty list
    to_delete = list()
    for k in nodes:
        if nodes[k] in wall:
            if wall[nodes[k]]["current"] == 0:
                # print("caught {} at depth {}".format(k, nodes[k]))
                to_delete.append(k)

    # delete naughty list
    for val in to_delete:
        del nodes[val]

    # if node made it to end, identify it and crack a beer
    for k in nodes:
        if nodes[k] == max(wall.keys())+1:
            found = True
            print("First delay where score is 0: {}".format(k))
            break

    # lastly, move wall state forward one
    if not found:
        for x in wall:
            wall[x]["current"] = next(wall[x]["iter"])
        time += 1
