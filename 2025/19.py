from bisect import bisect_left, bisect_right
from collections import defaultdict, deque


def step(pos,next_gap=None): # new pos, cost (flaps)
    i,j = pos
    if next_gap is None:
        yield (i+1,j+1), 1
        yield (i+1,j-1), 0
    else:
        distance = next_gap - i
        yield from (((next_gap, j-distance+2*num_flaps), num_flaps) for num_flaps in range(distance+1))

def load_file(part):
    with open(f"everybody_codes_e2025_q19_p{part}.txt") as f:
        lines = f.read().splitlines()
    return [tuple(map(int,line.split(','))) for line in lines]

for part in (1,2):
    triplets = load_file(part)
    gaps = defaultdict(list)
    for dist, bottom_height, gap_size in triplets:
        gaps[dist].append(range(bottom_height, bottom_height + gap_size))

    last_gap = max(gaps)
    i_gaps = sorted(gaps)
    def next_i_gap(i):
        return i_gaps[bisect_right(i_gaps,i)]

    costs = {(0,0):0}
    q = deque([(0,0)])
    in_q = set(q)
    while q:
        p = q.popleft()
        in_q.remove(p)
        cost = costs[p]
        for np, c in step(p, next_gap=next_i_gap(p[0])):
            ni,nj = np
            if ni in gaps and all(nj not in gap for gap in gaps[ni]):
                continue
            costs[np] = min(cost + c, costs.get(np,10**10))
            if np[0] >= last_gap:
                continue
            if np not in in_q:
                q.append(np)
                in_q.add(np)
    print(min(c for (i,j),c in costs.items() if i == last_gap))