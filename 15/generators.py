gen_a_input = 277
gen_b_input = 349


def advent_generator(value, factor):
    while True:
        value = value * factor
        value = value % 2147483647
        yield value


gen_a = advent_generator(gen_a_input, 16807)
gen_b = advent_generator(gen_b_input, 48271)


count = 0

for x in range(40000000):
    if next(gen_a) & 65535 == next(gen_b) & 65535:
        count += 1

print("judge's count: {}".format(count))
