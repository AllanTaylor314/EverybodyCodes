def load_file(part):
    with open(f"everybody_codes_e2_q03_p{part}.txt") as f:
        lines = f.read().splitlines()
    out = {}
    grid = []
    for line in lines:
        if "=" in line:
            a,b,c = line.split()
            out[int(a[:-1])] = Die(eval(b.split("=")[1]), int(c.split("=")[1]))
        elif line:
            grid.append(list(map(int,line)))
    return out, grid

class Die:
    def __init__(self, faces, seed):
        self.seed = seed
        self.faces = faces
        self.pulse = seed
        self.roll_number = 1
        self.face = 0
        self.spin = 0
    def roll(self):
        self.spin = self.roll_number * self.pulse
        self.face += self.spin
        self.face %= len(self.faces)
        self.pulse += self.spin
        self.pulse %= self.seed
        self.pulse += 1 + self.roll_number + self.seed
        self.roll_number += 1
        return self.faces[self.face]
    def reset(self):
        self.pulse = self.seed
        self.roll_number = 0
        self.face = 0
    def __repr__(self):
        return f"<{self.roll_number} {self.spin} {self.faces[self.face]} {self.pulse}>"

dice = load_file(1)[0]
total = 0
count = 0
while total < 10000:
    for d in dice.values():
        total += d.roll()
    count += 1
print(count)

dice, grid = load_file(2)
track = grid[0]
for player_id, die in dice.items():
    i = 0
    while i < len(track):
        if die.roll() == track[i]:
            i+=1
print(*sorted(dice, key=lambda k: dice[k].roll_number),sep=",")

dice, grid = load_file(3)

all_possible_paths = [[False for _ in row] for row in grid]
cell_coordinates = {i:[] for i in range(1,10)}
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        cell_coordinates[cell].append((i,j))

for d in dice.values():
    possible_paths = [[{0} for _ in row] for row in grid]
    survives = True
    while survives:
        value = d.roll()
        print(d)
        survives = False
        for i,j in cell_coordinates[value]:
            neighbours = set(possible_paths[i][j])
            if i > 0:
                neighbours |= possible_paths[i-1][j]
            if i < len(grid) - 1:
                neighbours |= possible_paths[i+1][j]
            if j > 0:
                neighbours |= possible_paths[i][j-1]
            if j < len(row) - 1:
                neighbours |= possible_paths[i][j+1]
            if (d.roll_number - 2 in neighbours):
                possible_paths[i][j].add(d.roll_number - 1)
                survives = True
    for i, row in enumerate(possible_paths):
        for j, cell in enumerate(row):
            if len(cell) > 1:
                all_possible_paths[i][j] = True
print(sum(cell for row in all_possible_paths for cell in row))