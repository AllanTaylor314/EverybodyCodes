from functools import cache

DELTAS = {"+":+1,"-":-2,".":-1}
CHECKPOINTS = [None, "A", "B", "C", "S"]
CHECKPOINTS_MAP = {k:v for k,v in zip(CHECKPOINTS,CHECKPOINTS[1:])}
CHECKPOINTS_IMAP = {k:v for v,k in CHECKPOINTS_MAP.items()} | {None:None}
CHECKPOINTS_MAP["S"] = "S"

def load_file(part):
    with open(f"everybody_codes_e2024_q20_p{part}.txt") as f:
        lines = f.read().splitlines()
    return {(i,j):c for i,line in enumerate(lines) for j,c in enumerate(line)}

def adjacent_spaces(point):
    i, j = point
    return [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]

@cache
def fly(location,prev_location,remaining_time):
    c = grid.get(location,"#")
    if c == "#":
        return -10**10 # Crash and die
    if remaining_time == 0:
        return DELTAS[c]
    adjs = adjacent_spaces(location)
    if prev_location is not None:
        adjs.remove(prev_location)
    return DELTAS[c] + max(fly(next_loc,location,remaining_time-1) for next_loc in adjs)

altitude = 10000
time = 100
grid = load_file(2)
grid_locs = {v:k for k,v in grid.items() if v.isalpha()}

start = grid_locs["S"]
cpa = grid_locs["A"]
cpb = grid_locs["B"]
cpc = grid_locs["C"]

def next_states(state):
    prev,curr,check = state
    adjs = [p for p in adjacent_spaces(curr) if p != prev and grid.get(p,"#") != "#"]
    next_check = CHECKPOINTS_MAP[check]
    if curr == grid_locs[next_check]:
        check = next_check
    return [(curr,new,check) for new in adjs]

def prev_states(state):
    prev,curr,check = state
    if prev is None:
        return []
    adjs = [p for p in adjacent_spaces(prev) if p != curr and grid.get(p,"#") != "#"]
    adjs.append(None)
    prev_check = CHECKPOINTS_IMAP[check]
    if check is not None and prev == grid_locs[check]:
        check = prev_check
    return [(new,prev,check) for new in adjs]

locations_of_interest = (start,cpa,cpb,cpc,start)
start_state = (None,start,None)
target_prev = next_states(start_state)[0][1]
target_state = (target_prev, start, "C")
to_update = set()
costs = {}
costs[start_state] = 0
to_update.update(next_states(start_state))
while to_update:
    new_update = set()
    for state in to_update:
        prev,curr,check = state
        adjs = prev_states(state)
        new_cost = min([costs.get(adj,1e8) + 1 - DELTAS.get(grid[adj[1]],-1) for adj in adjs] or [1e8])
        if new_cost < costs.get(state,1e8):
            costs[state] = new_cost
            new_update.update(next_states(state))
    to_update = new_update

print(costs[target_state])
