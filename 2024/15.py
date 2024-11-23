from collections import defaultdict
from itertools import permutations
from functools import cache

DIRECTIONS = [(-1,0),(0,-1),(0,1),(1,0)]

def load_file(part):
    with open(f"everybody_codes_e2024_q15_p{part}.txt") as f:
        return {(i,j):c for i,row in enumerate(f.read().splitlines()) for j,c in enumerate(row) if c not in "#~"}

def add_points(*points):
    return tuple(map(sum,zip(*points)))

@cache
def min_cost_order(current,remaining_herbs,end):
    if not remaining_herbs:
        return all_costs[current][end]
    next_herb = remaining_herbs[0]
    next_locations = herb_locations[next_herb]
    return min(all_costs[current][next_loc]+min_cost_order(next_loc,remaining_herbs[1:],end) for next_loc in next_locations)

for part in (1,2,3):
    min_cost_order.cache_clear()
    grid = load_file(part)
    start = min(grid)
    herb_locations = defaultdict(list)
    for p,v in grid.items():
        if v.isalpha():
            herb_locations[v].append(p)

    required_locations = [start]
    required_locations.extend(loc for herb,locs in herb_locations.items() for loc in locs)
    all_costs = {}
    for base_location in required_locations:
        all_costs[base_location] = costs = {location:1e8 for location in grid}
        costs[base_location] = 0
        to_update = {p for delta in DIRECTIONS if (p:=add_points(base_location,delta)) in grid}
        while to_update:
            new_update = set()
            for loc in to_update:
                neighbours = [p for delta in DIRECTIONS if (p:=add_points(loc,delta)) in grid]
                neighbour_costs = map(costs.get,neighbours)
                new_cost = min(neighbour_costs) + 1
                if new_cost < costs[loc]:
                    costs[loc] = new_cost
                    new_update.update(neighbours)
            to_update = new_update
    if part < 3:
        print(min(min_cost_order(start,perm,start) for perm in permutations(herb_locations)))

mid_e = max(herb_locations["E"])
mid_r = min(herb_locations["R"])
abcde = min(min_cost_order(mid_e,perm,mid_e) for perm in permutations("ABCDE"))
ghijk = min(min_cost_order(start,perm,start) for perm in permutations("EGHIJKR"))
nopqr = min(min_cost_order(mid_r,perm,mid_r) for perm in permutations("NOPQR"))
print(abcde+ghijk+nopqr)
