from collections import defaultdict
from itertools import permutations

DIRECTIONS = [(-1,0),(0,-1),(0,1),(1,0)]

def load_file(part):
    with open(f"everybody_codes_e2024_q15_p{part}.txt") as f:
        return {(i,j):c for i,row in enumerate(f.read().splitlines()) for j,c in enumerate(row) if c not in "#~"}

def add_points(*points):
    return tuple(map(sum,zip(*points)))

grid = load_file(2)
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

def cost_of_path(path):
    """Start -> herb -> herb -> start"""
    return sum(all_costs[a][b] for a,b in zip(path,path[1:]))

def gen_all_combos(list_of_lists, prefix=None):
    if prefix is None:
        prefix = []
    if list_of_lists:
        list0, *other_lists = list_of_lists
        for value in list0:
            yield from gen_all_combos(other_lists, prefix + [value])
    else:
        yield prefix

def gen_viable_paths():
    herbs = list(herb_locations)
    for herb_order in permutations(herbs):
        order = [[start]] + [herb_locations[herb] for herb in herb_order] + [[start]]
        for combo in gen_all_combos(order):
            yield combo

print(min(map(cost_of_path,gen_viable_paths())))

def display_costs(costs):
    maxi = max(loc[0] for loc in costs) + 1
    maxj = max(loc[1] for loc in costs) + 1
    for i in range(maxi):
        for j in range(maxj):
            print(end=f"{costs.get((i,j)):4d}" if (i,j) in costs else "####")
        print()
