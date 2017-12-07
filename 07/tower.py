programs = []

def set_weights(program):
    weight = program['value']
    child_weights = []
    for child in program['children']:
        child_weights.append(set_weights([x for x in programs if x['name'] == child][0]))
    if len(child_weights) > 0:
        weight += sum(child_weights)
    program['weight'] = weight
    program['child_weights'] = child_weights
    return weight

def get_from_parens(s) -> int:
    return int(s[s.find("(")+1:s.find(")")])


with open("input1.txt") as file:
    for row in file:
        if "->" not in row:
            name = row.split()[0]
            value = get_from_parens(row.split()[1])
            programs.append(dict(name=name, children=[], value=value))
        else:
            name = row.split()[0]
            value = get_from_parens(row.split()[1])
            child_list = [x.strip() for x in row.split("->")[1].split(",")]
            programs.append(dict(name=name, children=child_list, value=value))

# set up parents in tree

for program in programs:
    if len(program['children']) > 0:
        for child_program in program['children']:
            [x for x in programs if x['name'] == child_program][0]['parent'] = program['name']

# part 1

print([x['name'] for x in programs if 'parent' not in x])

# part 2

for prog in programs:
    set_weights(prog)

print([x for x in programs if len(set(x['child_weights'])) > 1])

