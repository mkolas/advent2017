tape = dict()
cursor = 0
state_ = "a"
steps = 12302209
# steps = 6
leftmost = 0
rightmost = 0

def create_if_not_exists(position):
    if position not in tape:
        tape[position] = 0

def update_bounds(position):
    global leftmost
    global rightmost
    if position < leftmost:
        leftmost = position
    if position > rightmost:
        rightmost = position

def write(num):
    global cursor
    tape[cursor] = num

def left():
    global cursor
    cursor -= 1

def right():
    global cursor
    cursor += 1

def state(s):
    global state_
    state_ = s


for x in range(steps):
    print(x)
    create_if_not_exists(cursor)
    update_bounds(cursor)
    if state_ is 'a':
        if tape[cursor] == 0:
            write(1)
            right()
            state('b')
        else:
            write(0)
            left()
            state('d')
        continue
    if state_ is 'b':
        if tape[cursor] == 0:
            write(1)
            right()
            state('c')
        else:
            write(0)
            right()
            state('f')
        continue
    if state_ is 'c':
        if tape[cursor] == 0:
            write(1)
            left()
        else:
            write(1)
            left()
            state('a')
        continue
    if state_ is 'd':
        if tape[cursor] == 0:
            write(0)
            left()
            state('e')
        else:
            write(1)
            right()
            state('a')
        continue
    if state_ is 'e':
        if tape[cursor] == 0:
            write(1)
            left()
            state('a')
        else:
            write(0)
            right()
            state('b')
        continue
    if state_ is 'f':
        if tape[cursor] == 0:
            write(0)
            right()
            state('c')
        else:
            write(0)
            right()
            state('e')
        continue

count = 0
for x in range(leftmost, rightmost+1):
    if tape[x] == 1:
        count += 1

print(count)