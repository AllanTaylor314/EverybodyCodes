from collections import deque
from itertools import zip_longest


def adj(p):
    i,j = p
    yield i,j-1
    yield i,j+1
    if j % 2: # ^
        yield i + 1, j - 1
    else: # v
        yield i - 1, j + 1

assert set(adj((0,1))) == {(0,0),(0,2),(1,0)}
assert set(adj((1,1))) == {(1,0),(1,2),(2,0)}
assert set(adj((1,2))) == {(1,1),(0,3),(1,3)}


def load_file(part):
    with open(f"everybody_codes_e2025_q20_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines

grid = load_file(1)
grid = [l.strip('.') for l in grid]

grid_dict = {}
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        grid_dict[i,j] = cell

total = 0
for p, cell in grid_dict.items():
    if cell == 'T':
        for a in adj(p):
            total += grid_dict.get(a) == 'T'
print(total // 2)

#################################################

grid = load_file(2)
grid = [l.strip('.') for l in grid]

grid_dict = {}
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == 'S':
            start = i,j
            cell = 'T'
        elif cell == 'E':
            end = i,j
            cell = 'T'
        grid_dict[i,j] = cell

costs = {}
for p, cell in grid_dict.items():
    if cell == 'T':
        costs[p] = 10**10
costs[start] = 0

q = deque([start])
in_q = set(q)
while q:
    p = q.popleft()
    in_q.remove(p)
    cost = costs[p] + 1
    for a in adj(p):
        if a in costs and cost < costs[a]:
            costs[a] = cost
            if a not in in_q:
                q.append(a)
                in_q.add(a)
print(costs[end])

#################################################

grid = load_file(3)
grid = [l.strip('.') for l in grid]

def rotate_coord(p):
    return rotation_grid.get(p)

def adjr(p):
    yield rotate_coord(p) # in place
    for a in adj(p):
        yield rotate_coord(a)

grid_dict = {}
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == 'S':
            start = i,j
            cell = 'T'
        elif cell == 'E':
            end = i,j
            cell = 'T'
        grid_dict[i,j] = cell

temp_rotation_grid = [[(i,j) for j, cell in enumerate(row)] for i,row in enumerate(grid)]
temp_rotation_grid = [row[e::2] for row in temp_rotation_grid for e in (0,1)]
temp_rotation_grid.reverse()
temp_rotation_grid = [list(filter(None,r)) for r in zip_longest(*temp_rotation_grid)]
rotation_grid = {(i,j):d for i,row in enumerate(temp_rotation_grid) for j,d in enumerate(row)}

costs = {}
for p, cell in grid_dict.items():
    if cell == 'T':
        costs[p] = 10**10
costs[start] = 0

q = deque([start])
in_q = set(q)
while q:
    p = q.popleft()
    in_q.remove(p)
    cost = costs[p] + 1
    for a in adjr(p):
        if a in costs and cost < costs[a]:
            costs[a] = cost
            if a not in in_q:
                q.append(a)
                in_q.add(a)
print(costs[end])
