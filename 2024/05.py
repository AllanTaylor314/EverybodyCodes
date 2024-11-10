from itertools import zip_longest

with open("everybody_codes_e2024_q5_p1.txt") as f:
    lines = f.read().splitlines()
nums = [list(map(int,line.split())) for line in lines]
cols = list(map(list,zip(*nums)))

for r in range(10):
    clapper_column = r%len(cols)
    clapper = cols[clapper_column].pop(0)
    target_col = cols[(clapper_column+1)%len(cols)]
    position = (clapper - 1) % (2*len(target_col))
    if position >= len(target_col):
        position = 2*len(target_col) - position
    target_col.insert(position,clapper)
    print(f"Round {r+1}")
    for row in zip_longest(*cols,fillvalue=" "):
        print(*row)
print(*(col[0] for col in cols))
