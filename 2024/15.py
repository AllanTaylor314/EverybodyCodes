DIRECTIONS = [(-1,0),(0,-1),(0,1),(1,0)]

def load_file(part):
    with open(f"everybody_codes_e2024_q15_p{part}.txt") as f:
        return {(i,j):c for i,row in enumerate(f.read().splitlines()) for j,c in enumerate(row) if c!="#"}

def add_points(*points):
    return tuple(map(sum,zip(*points)))

grid = load_file(1)
start = min(grid)
ends = [p for p,v in grid.items() if v.isalpha()]

costs = {location:0 if location == start else 1e8 for location in grid}
to_update = {add_points(start,(1,0))}
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

print(min(costs[p] for p in ends))
