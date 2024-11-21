def load_file(part):
    with open(f"everybody_codes_e2024_q13_p{part}.txt") as f:
        return f.read().splitlines()

def adjacent_spaces(point):
    i, j = point
    return [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]

def valid_adjacent_spaces(point):
    return [p for p in adjacent_spaces(point) if p in grid]

def min_transition(a,b):
    return min(abs(a-b),abs(10-a+b),abs(10-b+a))

for part in (1,2,3):
    lines = load_file(part)
    grid = {(i,j):c for i,line in enumerate(lines) for j,c in enumerate(line) if c not in "# "}

    starts = [k for k,v in grid.items() if v=="S"]
    end ,= (k for k,v in grid.items() if v=="E")
    grid = {k:int(v) if v.isnumeric() else 0 for k,v in grid.items()}

    costs = {p:1e80 for p in grid}
    costs[end] = 0
    updated = True
    while updated:
        updated = False
        for point in costs:
            adjs = valid_adjacent_spaces(point)
            new_cost = min([costs[adj] + min_transition(grid[point],grid[adj])+1 for adj in adjs] or [1e8])
            if new_cost < costs[point]:
                costs[point] = new_cost
                updated = True
    print(min(costs[start] for start in starts))
