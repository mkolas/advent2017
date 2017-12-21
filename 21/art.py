from math import ceil

import copy

rules = dict()
an_art = ["#.", "..#", "###"]


def text_to_art(text):
    return text.split("/")


def art_to_text(art):
    return "/".join(art)


def flip_h(art):
    for line in art:
        i = 0
        while i < len(line)/2:
            line[i], line[len(line)-1-i] = line[len(line)-1-i], line[i]
            i += 1
    return art


def flip_v(art):
    return art[::-1]


def rotate_r(art):
    return [list(a) for a in zip(*flip_v(art))]


def chunk_art(art):
    chunks = list()
    if len(art) == 2 or len(art) == 3:
        return art
    if len(art) % 2 == 0:
        chunk_row = list()
        rows_to_chunk = art[:2]
        art = art[2:]
        while len(rows_to_chunk[0]) > 0:

        chunk_row.append()
    quarters.append([y[:ceil(len(y)/2)] for i, y in enumerate(art) if i < len(art) / 2])
    quarters.append([y[ceil(len(y)/2):] for i, y in enumerate(art) if i < len(art) / 2])
    quarters.append([y[:ceil(len(y)/2)] for i, y in enumerate(art) if i >= len(art) / 2])
    quarters.append([y[ceil(len(y)/2):] for i, y in enumerate(art) if i >= len(art) / 2])
    return quarters



def print_art(art):
    for line in art:
        print(''.join(line), "\n")


with open("test.txt") as f:
    for row in f:
        row_items = row.split("=>")
        rule_art = text_to_art(row_items[0].strip())
        rule_target = text_to_art(row_items[1].strip())
        for x in range(4):  # rotate vanilla
            rule_art = rotate_r(rule_art)
            rules[art_to_text(rule_art)] = rule_target

        v_art = flip_v(rule_art)
        for x in range(4):  # rotate  v flip
            v_art = rotate_r(v_art)
            rules[art_to_text(v_art)] = rule_target

        h_art = flip_h(rule_art)
        for x in range(4):  # rotate h flip
            h_art = rotate_r(h_art)
            rules[art_to_text(h_art)] = rule_target

        vh_art = flip_h(flip_v(rule_art))
        for x in range(4):  # rotate v+h flip
            rule_art = rotate_r(vh_art)
            rules[art_to_text(vh_art)] = rule_target


for x in range(5):
    print("iteration ", x)
    art_chunks = chunk_art(an_art)
    if len(art_chunks) == 1:
        an_art = rules[art_to_text(art_chunks[0])]
    else:
        new_art = list()
        for an_chunk in art_chunks:
            new_chunk = rules[art_to_text(an_chunk)]
            new_art = assemble_art(new_art, new_chunk)
        an_art = new_art
    print_art(an_art)

