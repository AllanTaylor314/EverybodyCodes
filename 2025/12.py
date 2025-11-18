from collections import deque

def adj(cell):
    i,j = cell
    yield i+1,j
    yield i-1,j
    yield i,j+1
    yield i,j-1

def load_file(part):
    with open(f"everybody_codes_e2025_q12_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines#list(map(int, lines))

grid = load_file(1)
grid_dict = {}
for i,line in enumerate(grid):
    for j,c in enumerate(line):
        grid_dict[i,j] = int(c)

q = deque([(0,0)])
hits = {(0,0)}
while q:
    p = q.popleft()
    for a in adj(p):
        if grid_dict[p] >= grid_dict.get(a,10):
            if a not in hits:
                hits.add(a)
                q.append(a)
print(len(hits))

grid = load_file(2)
grid_dict = {}
for i,line in enumerate(grid):
    for j,c in enumerate(line):
        grid_dict[i,j] = int(c)

q = deque([(0,0),(i,j)])
hits = {(0,0)}
while q:
    p = q.popleft()
    for a in adj(p):
        if grid_dict[p] >= grid_dict.get(a,10):
            if a not in hits:
                hits.add(a)
                q.append(a)
print(len(hits))

grid = load_file(3)
grid_dict = {}
for i,line in enumerate(grid):
    for j,c in enumerate(line):
        grid_dict[i,j] = int(c)

destroyable_barrels = {p:{p} for p in grid_dict}
q = deque(grid_dict)
in_q = set(q)
n = 0
while q:
    p = q.popleft()
    in_q.remove(p)
    new = destroyable_barrels[p]
    old_len = len(new)
    for a in adj(p):
        if grid_dict[p] >= grid_dict.get(a,10):
            new |= destroyable_barrels[a]
    if len(new) > old_len:
        for a in adj(p):
            if grid_dict[p] <= grid_dict.get(a,-1) and a not in in_q:
                q.append(a)
                in_q.add(a)
    n += 1
    if n%100000 == 0:
        print(n,p,len(new))

destroyed_barrels = set()
for _ in range(3):
    loc = max(destroyable_barrels,key=lambda p:len(destroyable_barrels[p]))
    print("Destroy",loc)
    destroyed_barrels |= destroyable_barrels[loc]
    for v in destroyable_barrels.values():
        v -= destroyed_barrels
print(len(destroyed_barrels))