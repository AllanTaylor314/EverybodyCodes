from itertools import cycle

def load_file(part):
    with open(f"everybody_codes_e2024_q19_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines

def adjacent_spaces(point):
    i, j = point
    return [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1)]

def flatten(grid):
    return "\n".join(map("".join,grid))

def rotate(grid, point, direction):
    adj = adjacent_spaces(point)
    vals = [grid[i][j] for (i,j) in adj]
    if direction == "L":
        adj = adj[-1:]+adj[:-1]
    elif direction == "R":
        adj = adj[1:]+adj[:1]
    else:
        raise ValueError
    for (i,j),c in zip(adj,vals):
        grid[i][j] = c

pattern,_,*lines = load_file(2)
grid = [list(line) for line in lines]
rotation_points = [(i,j) for i in range(1,len(grid)-1) for j in range(1,len(grid[i])-1)]

for _ in range(100):
    for d, p in zip(cycle(pattern), rotation_points):
        rotate(grid, p, d)

print(flatten(grid))
