from itertools import cycle

TARGETS = {1:1, 2:100, 3:1048576000}

def load_file(part):
    with open(f"everybody_codes_e2024_q19_p{part}.txt") as f:
        pattern,_,*lines = f.read().splitlines()
    return pattern,lines

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

def is_adj(point1, point2):
    return max(abs(a-b) for a,b in zip(point1,point2))==1

for part in (1,2,3):
    target = TARGETS[part]
    pattern,lines = load_file(part)
    grid = [list(line) for line in lines]
    rotation_points = [(i,j) for i in range(1,len(grid)-1) for j in range(1,len(grid[i])-1)]

    loc_grid = [[(i,j) for j,c in enumerate(line)] for i,line in enumerate(lines)]
    for d, p in zip(cycle(pattern), rotation_points):
        rotate(loc_grid, p, d)
    mappings = {}
    mappings[1] = {(i,j):(oi,oj) for i,l in enumerate(loc_grid) for j,(oi,oj) in enumerate(l)}
    mapping_size = 1
    while mapping_size < target:
        pmp = mappings[mapping_size]
        mapping_size *= 2
        mappings[mapping_size] = {k:pmp[v] for k,v in pmp.items()}

    required_mappings = [k for k in mappings if k&target]

    new_grid = [line.copy() for line in grid]

    for i,line in enumerate(grid):
        for j,c in enumerate(line):
            oi,oj = i,j
            for rm in required_mappings:
                oi,oj = mappings[rm][oi,oj]
            new_grid[i][j] = grid[oi][oj]
    solution = flatten(new_grid)
    # Remove next line for full picture
    solution = solution[solution.index(">")+1:solution.index("<")]
    print(solution)
