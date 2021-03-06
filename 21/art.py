import copy
from math import ceil

rules = dict()
an_art = [".#.", "..#", "###"]


def text_to_art(text):
    return text.split("/")


def art_to_text(art):
    return "/".join(art)


def flip_h(art):
    reversed_ = list()
    for line in art:
        reversed_.append(line[::-1])
    return reversed_


def flip_v(art):
    return art[::-1]


def rotate_r(art):
    return [''.join(list(a)) for a in zip(*flip_v(art))]


def chunk_art(art):
    chunks = list()
    if len(art) == 2 or len(art) == 3:
        chunks.append(art)
        return chunks
    if len(art) % 2 == 0:
        while len(art) > 0:
            chunk_row = list()
            rows_to_chunk = art[:2]
            art = art[2:]
            while len(rows_to_chunk[0]) > 0:
                chunk = [rows_to_chunk[0][:2], rows_to_chunk[1][:2]]
                chunk_row.append(chunk)
                rows_to_chunk[0] = rows_to_chunk[0][2:]
                rows_to_chunk[1] = rows_to_chunk[1][2:]
            chunks.append(chunk_row)
        return chunks
    elif len(art) % 3 == 0:
        while len(art) > 0:
            chunk_row = list()
            rows_to_chunk = art[:3]
            art = art[3:]
            while len(rows_to_chunk[0]) > 0:
                chunk = [rows_to_chunk[0][:3], rows_to_chunk[1][:3], rows_to_chunk[2][:3]]
                chunk_row.append(chunk)
                rows_to_chunk[0] = rows_to_chunk[0][3:]
                rows_to_chunk[1] = rows_to_chunk[1][3:]
                rows_to_chunk[2] = rows_to_chunk[2][3:]
            chunks.append(chunk_row)
        return chunks


def init_rows(size):
    return_rows = list()
    for s in range(size):
        return_rows.append("")
    return return_rows


def combine_row(chunk_row):
    return_rows = init_rows(len(rules[art_to_text(chunk_row[0])]))
    for chunk in chunk_row:
        transformed_chunk = rules[art_to_text(chunk)]
        for i, r in enumerate(transformed_chunk):
            return_rows[i] += r
    return return_rows


def print_art(art):
    for line in art:
        print(line, "\n")


def count_hashes(art):
    count = 0
    for row in an_art:
        for char in row:
            if char is '#':
                count += 1
    return count


with open("input1.txt") as f:
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


for x in range(18):
    art_chunks = chunk_art(an_art)
    if len(art_chunks) == 1:
        new_art = rules[art_to_text(art_chunks[0])]
    else:
        new_art = list()
        for row in art_chunks:
            new_rows = combine_row(row)
            for nr in new_rows:
                new_art.append(nr)
    an_art = new_art
    if x == 4:
        print("Num #s after 5 iterations: ", count_hashes(an_art))
    # print_art(an_art)


print("Num #s after 18 iterations: ", count_hashes(an_art))
