from collections import defaultdict, deque
from itertools import chain, permutations
from math import prod

def parse_line(line):
    scale, dna = line.split(':')
    return int(scale),dna

def load_file(part):
    with open(f"everybody_codes_e2025_q09_p{part}.txt") as f:
        return [line.split(':')[1] for line in f.read().splitlines()]

def load_file3():
    with open(f"everybody_codes_e2025_q09_p3.txt") as f:
        return dict(map(parse_line,f.read().splitlines()))

sequences = load_file(1)
for i,child in enumerate(sequences):
    parents = [d for j,d in enumerate(sequences) if i != j]
    matches = [0]*len(parents)
    for c,*ps in zip(child,*parents):
        if c not in ps:
            break
        for j,p in enumerate(ps):
            matches[j] += c==p
    else:
        print(prod(matches))
        break

sequences = load_file(2)
total = 0
for child,*parents in permutations(sequences,3):
    if parents[0] > parents[1]: continue # Skip duplicates
    matches = [0]*len(parents)
    for c,*ps in zip(child,*parents):
        if c not in ps:
            break
        for j,p in enumerate(ps):
            matches[j] += c==p
    else:
        total += prod(matches)
print(total)

sequences = load_file3()
child_to_parents = defaultdict(tuple)
parent_to_children = defaultdict(list)
for child,*parents in permutations(sequences.items(),3):
    if child[0] in child_to_parents: continue
    if parents[0][1] > parents[1][1]: continue # Skip duplicates
    matches = [0]*len(parents)
    for c,*ps in zip(child[1],*(p[1] for p in parents)):
        if c not in ps:
            break
    else:
        # print(parents,child)
        child_to_parents[child[0]] = tuple(p[0] for p in parents)
        for parent in parents:
            parent_to_children[parent[0]].append(child[0])
# print('Starting tree building')
unused = set(sequences.keys())
size_sums = []
while unused:
    seed = unused.pop()
    family = {seed}
    q = deque([seed])
    while q:
        member = q.popleft()
        for rel in chain(child_to_parents[member],parent_to_children[member]):
            if rel not in family:
                q.append(rel)
            unused.discard(rel)
            family.add(rel)
    size_sums.append((len(family),sum(family)))
    # print(size_sums)

print(max(size_sums)[1])