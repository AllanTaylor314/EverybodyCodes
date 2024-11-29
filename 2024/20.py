from functools import cache

DELTAS = {"+":+1,"-":-2,".":-1,"S":0}

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

altitude = 1000
time = 100
grid = load_file(1)

start ,= ((ij) for ij,c in grid.items() if c == "S")
si,sj = start
print(altitude + fly(start,None,100))

# not 1063 (CC)
