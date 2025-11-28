from bisect import bisect_right
from collections import defaultdict

def reachable_range(current_range, distance):
    lower, upper = current_range
    lower -= distance
    upper += distance
    return lower, upper

def range_intersect(rng1, rng2):
    l1, u1 = rng1
    l2, u2 = rng2
    l = max(l1,l2)
    u = min(u1,u2)
    if l <= u:
        return l, u

def range_union(rng1, rng2):
    l1, u1 = rng1
    l2, u2 = rng2
    if range_intersect(rng1, rng2):
        return min(l1,l2),max(u1,u2)

def union_ranges(rngs):
    rngs = sorted(rngs)
    out = []
    for rng in rngs:
        if out:
            un = range_union(out[-1], rng)
            if un:
                out[-1] = un
            else:
                out.append(rng)
        else:
            out.append(rng)
    return out

def intersect_ranges(rngs1, rngs2):
    return union_ranges(filter(None,(range_intersect(rng1,rng2) for rng1 in rngs1 for rng2 in rngs2)))

def calc_cost(point):
    i,j = point
    if i%2 == j%2: # Only half the checkerboard
        return (i+j)//2

def load_file(part):
    with open(f"everybody_codes_e2025_q19_p{part}.txt") as f:
        lines = f.read().splitlines()
    return [tuple(map(int,line.split(','))) for line in lines]

for part in (1,2,3):
    triplets = load_file(part)
    gaps = defaultdict(list)
    for dist, bottom_height, i_gap_size in triplets:
        gaps[dist].append((bottom_height, bottom_height + i_gap_size - 1))

    i_gaps = sorted(gaps)

    prev_i = 0
    ranges = [(0,0)]
    for i_gap in i_gaps:
        ranges = intersect_ranges((reachable_range(r, i_gap - prev_i) for r in ranges), gaps[i_gap])
        prev_i = i_gap
    print(calc_cost((prev_i, next((j for l,u in ranges for j in range(l,u+1) if prev_i%2==j%2)))))
