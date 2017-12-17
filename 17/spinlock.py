spinlock = list([0])
step = 344
index = 0
counter = 0

# part 1

for x in range(2017):
    index = (index + step) % len(spinlock)
    counter += 1
    spinlock.insert(index+1, counter)
    index += 1

print(spinlock[index+1])

# part 2

index = 0

for x in range(50000000):
    index = (index + step) % (x+1)
    if index == 0:
        to_return = x+1
    index += 1

print(to_return)