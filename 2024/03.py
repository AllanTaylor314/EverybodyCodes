ADJ = [(0,-1),(0,1),(1,0),(-1,0)]
ADDJ = [(1,1),(-1,-1),(1,-1),(-1,1)]
def new_depth(i,j):
    dep = 1e100
    for di,dj in ADJ:
        ni = i+di
        nj = j+dj
        if ni<0 or ni>=len(depths) or nj<0 or nj>=len(depths[0]):
            dep = 0
        else:
            dep = min(dep,depths[ni][nj])
    return dep + 1

for part in [1,2,3]:
    if part == 3:
        ADJ += ADDJ
    with open(f"everybody_codes_e2024_q3_p{part}.txt") as f:
        lines = f.read().splitlines()
    depths = [[0]*len(line) for line in lines]
    locations = [(i,j) for i,line in enumerate(lines) for j,c in enumerate(line) if c=="#"]
    total = 0
    prev_total = -1
    while total != prev_total:
        for i,j in locations:
            depths[i][j] = new_depth(i,j)
        prev_total = total
        total = sum(map(sum,depths))
    print(total)
