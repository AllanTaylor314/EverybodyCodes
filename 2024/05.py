from collections import Counter
from itertools import zip_longest

with open("everybody_codes_e2024_q5_p2.txt") as f:
    lines = f.read().splitlines()
nums = [list(map(int,line.split())) for line in lines]
cols = list(map(list,zip(*nums)))

seen_numbers = Counter()
result = None
r = 0
while seen_numbers[result] < 2024:
    clapper_column = r%len(cols)
    clapper = cols[clapper_column].pop(0)
    target_col = cols[(clapper_column+1)%len(cols)]
    position = (clapper - 1) % (2*len(target_col))
    if position >= len(target_col):
        position = 2*len(target_col) - position
    target_col.insert(position,clapper)
    result = int("".join(str(col[0]) for col in cols))
    seen_numbers[result] += 1
    r += 1
print(result*r)
# Not 10111010 (wrong length, right first digit)
# Missed the multiply by num rounds
