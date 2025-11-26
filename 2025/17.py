from collections import defaultdict, deque
from itertools import chain


def load_file(part):
    with open(f"everybody_codes_e2025_q17_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines


def dist2(a,b):
    ai,aj = a
    bi,bj = b
    return (ai-bi)**2+(aj-bj)**2

grid = load_file(1)
mid ,= ((i,j) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell == '@')
print(sum(int(cell) for i,row in enumerate(grid) for j,cell in enumerate(row) if 0 < dist2((i,j),mid) <= 100))

grid = load_file(2)
mid ,= ((i,j) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell == '@')
radius_sums = defaultdict(int)
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        radius_sums[int(dist2((i,j),mid)**.5 - 0.0001)] += int(cell) if cell != '@' else 0
radius, total = max(radius_sums.items(),key=lambda p:p[1])
print((radius+1)*total)

grid = load_file(3)
mid ,= ((i,j) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell == '@')
start ,= ((i,j) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell == 'S')

grid_weights = {(i,j): int(cell) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell.isdigit()}
grid_weights[start] = 0

destruction_radius = {(i,j): int(dist2((i,j),mid)**.5 - 0.0001) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell != '@'}

# each grid cell will have a time to reach (+ time to use) & a minimum destruction time
# state is probably (i,j,min_time): time_to_reach, except that doesn't account for the required overlap
# nor the bit where it needs to encompass the lava
# might be easier to just try for each radius (there are only 106)

# closed loop with @ inside => odd number of crossings in each direction (counting colinear is a pain)
# flood fill from @ to edge?

def adj(cell):
    i,j = cell
    yield i+1,j
    yield i-1,j
    yield i,j+1
    yield i,j-1

# search for a line to the left and a line to the right (still needs to zig zag a bit)
radius = 5
def p3(radius, plot=False):
    states = defaultdict(lambda:(10**10,None))
    min_time = 30 * radius
    states[start] = (0,None)
    q = deque(adj(start))
    in_q = set(q)
    while q:
        p = q.popleft()
        in_q.remove(p)
        try:
            best, best_adj = min((states.get(a, (10**10,))[0], a) for a in adj(p) if destruction_radius.get(a,0) >= radius)
        except ValueError:
            best = 10**10
            best_adj = None
        best += grid_weights.get(p, 10**10)
        if best < states[p][0]:
            states[p] = best, best_adj
            for a in adj(p):
                if destruction_radius.get(a,0) >= radius and a not in in_q:
                    q.append(a)
                    in_q.add(a)
            
    def trace_path(p):
        while p is not None:
            yield p
            weight, p = states[p]

    def path_direction(path):
        mi,mj = mid
        for i,j in path:
            if mi == i:
                return 'left' if j < mj else 'right'

    paths = {p:d for p in states if (d:=path_direction(trace_path(p)))}

    left_paths = {p for p,d in paths.items() if d == 'left'}
    right_paths = {p for p,d in paths.items() if d == 'right'}

    def gen_possible_weights():
        for l in left_paths:
            for a in adj(l):
                if a in right_paths:
                    yield states[l][0] + states[a][0], (l, a)
        yield float('inf'), (None, None)
    best, (pos1, pos2) = min(gen_possible_weights())
    # print(destruction_radius)
    if plot:
        plotting_grid = [[cell if destruction_radius.get((i,j),0) >= radius else '.' for j,cell in enumerate(row)] for i,row in enumerate(grid)]
        for i,j in chain(trace_path(pos1),trace_path(pos2)):
            plotting_grid[i][j] = ' '
        for row in plotting_grid:
            print(*row,sep='')
    return best

for radius in range(1,max(destruction_radius.values())):
    res = p3(radius)
    time = (radius+1)*30
    if res < time:
        p3(radius,True)
        print(radius * res)
        break
    print('#',radius,time,res)