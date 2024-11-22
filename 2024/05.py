from collections import Counter

def load_file(part):
    with open(f"everybody_codes_e2024_q5_p{part}.txt") as f:
        lines = f.read().splitlines()
    nums = [list(map(int,line.split())) for line in lines]
    cols = list(map(list,zip(*nums)))
    return cols

def step(r, cols):
    clapper_column = r%len(cols)
    clapper = cols[clapper_column].pop(0)
    target_col = cols[(clapper_column+1)%len(cols)]
    position = (clapper - 1) % (2*len(target_col))
    if position >= len(target_col):
        position = 2*len(target_col) - position
    target_col.insert(position,clapper)

def get_state(r, cols):
    return (r%len(cols),tuple(map(tuple,cols)))

cols = load_file(1)
for r in range(10):
    step(r, cols)
print(*(col[0] for col in cols),sep="")

cols = load_file(2)
seen_numbers = Counter()
result = None
r = 0
while seen_numbers[result] < 2024:
    step(r,cols)
    result = int("".join(str(col[0]) for col in cols))
    seen_numbers[result] += 1
    r += 1
print(result*r)

cols = load_file(3)
r = 0
highest = 0
states = set()
while (state := get_state(r, cols)) not in states:
    states.add(state)
    step(r, cols)
    result = int("".join(str(col[0]) for col in cols))
    if result > highest:
        highest = result
    r += 1
print(highest)
