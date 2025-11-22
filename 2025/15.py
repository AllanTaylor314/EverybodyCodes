from collections import defaultdict, deque

def adj(cell):
    i,j = cell
    yield i+1,j
    yield i-1,j
    yield i,j+1
    yield i,j-1

def load_file(part):
    with open(f"everybody_codes_e2025_q15_p{part}.txt") as f:
        line ,= f.read().splitlines()
    return line.split(',')

def turn(heading, lr):
    dr,dc = heading
    if lr == 'L':
        return -dc,dr
    return dc,-dr

def add(*pts):
    return tuple(map(sum,zip(*pts)))

steps = load_file(1) # also works for 2
# steps = 'R3,R4,L3,L4,R3,R6,R9'.split(',')
# steps = 'L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3'.split(',')
heading = (-1,0)
start = postion = (0,0)
walls = set()
for step in steps:
    dist = int(step[1:])
    heading = turn(heading, step[0])
    for _ in range(dist):
        postion = add(postion,heading)
        walls.add(postion)
end = postion
walls.remove(end)

def plot():
    rs, cs = zip(*walls)
    minr = min(rs)
    maxr = max(rs)
    minc = min(cs)
    maxc = max(cs)
    for r in range(minr,maxr+1):
        for c in range(minc,maxc+1):
            pt = r,c
            if pt == start:
                print(end='S')
            elif pt == end:
                print(end='E')
            elif pt in walls:
                print(end='#')
            else:
                print(end=' ')
        print()

# plot()

rs, cs = zip(*walls)
minr = min(rs) - 3
maxr = max(rs) + 3
minc = min(cs) - 3
maxc = max(cs) + 3

costs = defaultdict(lambda: 10**10)
costs[start] = 0
q = deque(adj(start))
in_q = set(q)
while q and costs[end] >= 10**10:
    # input(str(q))
    pt = q.popleft()
    r,c = pt
    if r < minr or r > maxr or c < minc or c > maxc:
        continue # Skip outside bounds
    in_q.remove(pt)
    if pt not in walls:
        new_cost = min(costs[a] for a in adj(pt)) + 1
        if new_cost < costs[pt]:
            costs[pt] = new_cost
            for a in adj(pt):
                if a not in in_q:
                    q.append(a)
                    in_q.add(a)
print(costs[end])


