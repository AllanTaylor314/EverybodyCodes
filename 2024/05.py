with open("everybody_codes_e2024_q5_p3.txt") as f:
    lines = f.read().splitlines()
nums = [list(map(int,line.split())) for line in lines]
cols = list(map(list,zip(*nums)))

result = None
r = 0
highest = 0
while True:
    clapper_column = r%len(cols)
    clapper = cols[clapper_column].pop(0)
    target_col = cols[(clapper_column+1)%len(cols)]
    position = (clapper - 1) % (2*len(target_col))
    if position >= len(target_col):
        position = 2*len(target_col) - position
    target_col.insert(position,clapper)
    result = int("".join(str(col[0]) for col in cols))
    if result > highest:
        highest = result
        print(highest)
    r += 1
