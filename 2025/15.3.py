from collections import defaultdict
import matplotlib.pyplot as plt
from itertools import pairwise
from functools import cache

INF = float('inf')

def adj(cell):
    i,j = cell
    yield i+1,j
    yield i-1,j
    yield i,j+1
    yield i,j-1

def diags(p):
    i, j = p
    yield i + 1, j + 1
    yield i - 1, j + 1
    yield i + 1, j - 1
    yield i - 1, j - 1

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

def mul(scalar, pt):
    return tuple(scalar * p for p in pt)

steps = load_file(3)
# steps = 'R3,R4,L3,L4,R3,R6,R9'.split(',')
# steps = 'L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3'.split(',')
heading = (-1,0)
start = postion = (0,0)
walls = [start]
turn_counts = {'L':0,'R':0}
for step in steps:
    dist = int(step[1:])
    heading = turn(heading, step[0])
    turn_counts[step[0]] += 1
    postion = add(postion, mul(dist, heading))
    # for _ in range(dist):
    #     postion = add(postion,heading)
    walls.append(postion)
end = postion # need to account for end still in walls!
# walls.remove(end)
# walls.pop()
# walls.append()

# Open up the start
nr,nc = walls[1]
cr,cc = walls[0]
dr = 0 if nr == cr else -1 if nr < cr else 1
dc = 0 if nc == cc else -1 if nc < cc else 1
walls[0] = cr + dr, cc + dc
# and end
pr,pc = walls[-2]
cr,cc = walls[-1]
dr = 0 if pr == cr else -1 if pr < cr else 1
dc = 0 if pc == cc else -1 if pc < cc else 1
walls[-1] = cr + dr, cc + dc

nodes = [d for w in walls for d in diags(w)]
nodes.append(start)
nodes.append(end)

def irange(start,end):
    if start <= end:
        return range(start,end+1)
    return range(start,end-1,-1)

def slow_intersect(a_start,a_end,b_start,b_end):
    asr,asc = a_start
    aer,aec = a_end
    bsr,bsc = b_start
    ber,bec = b_end
    line_a = {(r,c) for r in irange(asr,aer) for c in irange(asc,aec)}
    line_b = {(r,c) for r in irange(bsr,ber) for c in irange(bsc,bec)}
    return line_a & line_b

def intersects(a_start,a_end,b_start,b_end):
    asr,asc = a_start
    aer,aec = a_end
    bsr,bsc = b_start
    ber,bec = b_end
    asr,aer = sorted((asr,aer))
    asc,aec = sorted((asc,aec))
    bsr,ber = sorted((bsr,ber))
    bsc,bec = sorted((bsc,bec))
    if asr == aer and bsr == ber: # Parallel =
        return asr == bsr and (asc <= bsc <= aec or bsc <= asc <= bec)
    if asc == aec and bsc == bec: # Parallel ||
        return asc == bsc and (asr <= bsr <= aer or bsr <= asr <= ber)
    if asr == aer and bsc == bec: # Perpendicular -|
        return asc <= bsc <= aec and bsr <= asr <= ber
    if asc == aec and bsr == ber: # Perpendicular |-
        return asr <= bsr <= aer and bsc <= asc <= bec
    raise ValueError(f'idk {(a_start,a_end,b_start,b_end)}')
    
    

def intersects_any_wall(line_start, line_end):
    sr,sc = line_start
    er,ec = line_end
    assert sr == er or sc == ec # Check axis aligned
    for (wall_start,wall_end) in pairwise(walls):
        if intersects(line_start, line_end,wall_start,wall_end):
            # if not slow_intersect(line_start, line_end,wall_start,wall_end):
            #     print('bad isct',line_start, line_end,wall_start,wall_end)
            return True
    return False

def can_l_shape(line_start,line_end):
    sr,sc = line_start
    er,ec = line_end
    if not intersects_any_wall(line_start,(er,sc)) and not intersects_any_wall((er,sc),line_end):
        return True
    if not intersects_any_wall(line_start,(sr,ec)) and not intersects_any_wall((sr,ec),line_end):
        return True
    return False

@cache
def node_distance(node, other_node):
    ar,ac = node
    br,bc = other_node
    if can_l_shape(node, other_node):
        return abs(br-ar)+abs(bc-ac)
    return INF

adj_matrix = defaultdict(list)
print(f'{len(nodes)} nodes')
for i, node in enumerate(nodes):
    for j in range(i+1,len(nodes)):
        other_node = nodes[j]
        if node_distance(node, other_node) is not INF:
            adj_matrix[node].append(other_node)
            adj_matrix[other_node].append(node)
    print(i, node)

node_weights = {node:INF for node in nodes}
node_weights[start] = 0

to_be_confirmed = set(nodes)

while to_be_confirmed:
    best = min(to_be_confirmed,key=node_weights.get)
    to_be_confirmed.remove(best)
    weight = node_weights[best]
    print(best, weight)
    for a in adj_matrix[best]:
        dist = node_distance(best, a)
        if weight + dist < node_weights[a]:
            node_weights[a] = weight + dist
print(node_weights[end])

def plot():
    # minr = min(rs)
    # maxr = max(rs)
    # minc = min(cs)
    # maxc = max(cs)
    # for r in range(minr,maxr+1):
    #     for c in range(minc,maxc+1):
    #         pt = r,c
    #         if pt == start:
    #             print(end='S')
    #         elif pt == end:
    #             print(end='E')
    #         elif pt in walls:
    #             print(end='#')
    #         else:
    #             print(end=' ')
    #     print()
    ax = plt.axes()
    ax.plot(*zip(*walls))
    # ax.plot(*zip(*path))

# plot()

# rs, cs = zip(*walls)
# minr = min(rs) - 3
# maxr = max(rs) + 3
# minc = min(cs) - 3
# maxc = max(cs) + 3

# costs = defaultdict(lambda: 10**10)
# costs[start] = 0
# q = deque(adj(start))
# in_q = set(q)
# while q and costs[end] >= 10**10:
#     # input(str(q))
#     pt = q.popleft()
#     r,c = pt
#     if r < minr or r > maxr or c < minc or c > maxc:
#         continue # Skip outside bounds
#     in_q.remove(pt)
#     if pt not in walls:
#         new_cost = min(costs[a] for a in adj(pt)) + 1
#         if new_cost < costs[pt]:
#             costs[pt] = new_cost
#             for a in adj(pt):
#                 if a not in in_q:
#                     q.append(a)
#                     in_q.add(a)
# print(costs[end])


plot()
plt.show(block=False)
