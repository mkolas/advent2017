nodes = dict()


def search_for(source, target, graph, searched_nodes):
    # global searched_nodes
    if source == target:
        return True
    if target in graph[source]:
        return True
    for k in graph[source]:
        if k not in searched_nodes:
            searched_nodes.append(k)
            if search_for(k, target, graph, searched_nodes):
                return True
    return False


with open("input1.txt") as f:
    for row in f:
        from_ = row.split()[0]
        to = ''.join(row.split()[2:]).split(',')
        nodes[from_] = to

count = 0

# part 1

for key in nodes.keys():
    if search_for(key, '0', nodes, list()):
        count += 1

print(count)

# part 2

groups = list(['0'])
for key in nodes.keys():
    found = False
    for group in groups:
        if search_for(key, group, nodes, list()):
            found = True
            break
    if not found:
        groups.append(key)

print(len(groups))
