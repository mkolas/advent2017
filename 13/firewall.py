from itertools import cycle
import copy


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
with open("input1.txt") as f:
    for row in f:
        depth = int(row.split(":")[0])
        size = int(row.split(":")[1])
        wall[depth] = dict(size=size, current=0, iter=oscillate(range(size)))
        next(wall[depth]["iter"])


score = 0

for x in range(max(wall.keys())+1):
    if x in wall:
        if wall[x]["current"] == 0:
            score += wall[x]["size"]*x
    for y in wall:
        wall[y]["current"] = next(wall[y]["iter"])


print("Score: {}".format(score))


