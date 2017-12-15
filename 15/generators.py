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
    gen_a_num = bin(next(gen_a))
    gen_b_num = bin(next(gen_b))

    if gen_a_num[-16:] == gen_b_num[-16:]:
        count += 1

print("judge's count: {}".format(count))
