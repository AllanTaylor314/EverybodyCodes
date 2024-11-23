from collections import defaultdict
from itertools import permutations
from functools import cache

DIRECTIONS = [(-1,0),(0,-1),(0,1),(1,0)]

def load_file(part):
    with open(f"everybody_codes_e2024_q15_p{part}.txt") as f:
        return {(i,j):c for i,row in enumerate(f.read().splitlines()) for j,c in enumerate(row) if c not in "#~"}

def add_points(*points):
    return tuple(map(sum,zip(*points)))

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

@cache
def minmax_distance_between_herbs(herb1, herb2):
    gen = (all_costs[loc1][loc2] for loc1 in herb_locations[herb1] for loc2 in herb_locations[herb2])
    hi = lo = next(gen)
    for cost in gen:
        if cost > hi:
            hi = cost
        if cost < lo:
            lo = cost
    return lo, hi

@cache
def minmax_order(order):
    mini = maxi = 0
    for a,b in zip(order,order[1:]):
        lo, hi = minmax_distance_between_herbs(a,b)
        mini += lo
        maxi += hi
    return mini, maxi

@cache
def min_cost_order(current,remaining_herbs,end=None): # and back to start
    if end is None:
        end = start
    if not remaining_herbs:
        return all_costs[current][end]
    next_herb = remaining_herbs[0]
    next_locations = herb_locations[next_herb]
    return min(all_costs[current][next_loc]+min_cost_order(next_loc,remaining_herbs[1:],end) for next_loc in next_locations)

def gen_viable_paths():
    herbs = list(herb_locations)
    limit = 1e8
    for herb_order in ["ABCDEGHIJKNOPQR"]: # GHIKEDCBAJRPONQ
        order = [[start]] + [herb_locations[herb] for herb in herb_order] + [[start]]
        yield from gen_all_combos(order)

for part in (3,):
    minmax_distance_between_herbs.cache_clear()
    minmax_order.cache_clear()
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
    
    # print(min(map(cost_of_path,gen_viable_paths())))


mid_e = max(herb_locations["E"])
mid_r = min(herb_locations["R"])
ghijk = min(min_cost_order(start,perm,start) for perm in permutations("EGHIJKR"))
abcde = min(min_cost_order(mid_e,perm,mid_e) for perm in permutations("ABCDE"))
ponqr = min(min_cost_order(mid_r,perm,mid_r) for perm in permutations("PONQR"))
print(ghijk+abcde+ponqr)
