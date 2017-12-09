level = 0
score = 0
ignore = False
garbage = False
garbage_count = 0

# python is REALLY bad for switch cases

with open("input1.txt") as f:
    for row in f:
        for char in row:
            if ignore:
                ignore = False
                continue
            if char is "!":
                ignore = True
                continue
            if garbage:
                if char is ">":
                    garbage = False
                else:
                    garbage_count += 1
                continue
            if char is "<":
                garbage = True
            if char is "{":
                level += 1
            if char is "}":
                score += level
                level -= 1

print("score = " + str(score))
print("garbage_count = " + str(garbage_count))