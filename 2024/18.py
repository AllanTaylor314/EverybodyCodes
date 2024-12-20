def load_file(part):
    with open(f"everybody_codes_e2024_q18_p{part}.txt") as f:
        lines = f.read().splitlines()
        return {(i,j):c for i,line in enumerate(lines) for j,c in enumerate(line) if c != "#"}

def adjacent_spaces(point):
    i, j = point
    return [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]

def valid_adjacent_spaces(point):
    return [p for p in adjacent_spaces(point) if p in grid]

for part in (1,2,3):
    grid = load_file(part)

    palms = [k for k,v in grid.items() if v=="P"]

    all_costs = {}

    if part < 3:
        start_locs = [[min(grid),max(grid)][:part]]
    else:
        start_locs = [[palm] for palm in palms]

    for starts in start_locs:
        to_update = set()
        costs = {p:1e80 for p in grid}
        for start in starts:
            all_costs[start] = costs
            costs[start] = 0
            to_update.update(valid_adjacent_spaces(start))
        while to_update:
            new_update = set()
            for point in to_update:
                adjs = valid_adjacent_spaces(point)
                new_cost = min([costs[adj] + 1 for adj in adjs] or [1e8])
                if new_cost < costs[point]:
                    costs[point] = new_cost
                    new_update.update(adjs)
            to_update = new_update
    if part < 3:
        print(max(costs[palm] for palm in palms))
    else:
        points = [p for p,c in grid.items() if c=="."]
        total_costs = {point:sum(all_costs[palm][point] for palm in palms) for point in points}
        print(min(total_costs.values()))
