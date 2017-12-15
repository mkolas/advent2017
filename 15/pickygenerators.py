gen_a_input = 277
gen_b_input = 349


def picky_generator(value, factor, multiple):
    while True:
        value = value * factor
        value = value % 2147483647
        if value % multiple == 0:
            yield value


gen_a = picky_generator(gen_a_input, 16807, 4)
gen_b = picky_generator(gen_b_input, 48271, 8)


count = 0

for x in range(5000000):
    if next(gen_a) & 65535 == next(gen_b) & 65535:
        count += 1

print("judge's count: {}".format(count))


