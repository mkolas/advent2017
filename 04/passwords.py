# part 1

count = 0

with open("input1.txt") as file:
    for row in file:
        words = row.split()
        wordset = set(words)
        if len(words) == len(wordset):
            count += 1
print(count)

# part 2

count = 0

with open("input1.txt") as file:
    for row in file:
        words = row.split()
        wordset = set([''.join(sorted(x)) for x in row.split()])
        if len(words) == len(wordset):
            count += 1
print(count)