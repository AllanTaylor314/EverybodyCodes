from math import prod

def num_blocks_used(length,charms):
    return sum(len(range(charm-1,length,charm)) for charm in charms)

def load_file(part):
    with open(f"everybody_codes_e2025_q16_p{part}.txt") as f:
        line ,= f.read().splitlines()
    return list(map(int,line.split(',')))

charms = load_file(1)
cols = [0]*90
for charm in charms:
    for i in range(charm-1,90,charm):
        cols[charm] += 1
print(sum(cols))
print(num_blocks_used(90,charms))

cols = load_file(2)
charms = []
for charm in range(1,len(cols)):
    if all(cols[i] > 0 for i in range(charm-1,len(cols),charm)):
        for i in range(charm-1,len(cols),charm):
            cols[i] -= 1
        charms.append(charm)
print(prod(charms))
assert not any(cols)

cols = load_file(3)
num_blocks = 202520252025000
charms = []
for charm in range(1,len(cols)):
    if all(cols[i] > 0 for i in range(charm-1,len(cols),charm)):
        for i in range(charm-1,len(cols),charm):
            cols[i] -= 1
        charms.append(charm)
print(charms)

lower_bound = len(cols)
upper_bound = 1000000000000000
while lower_bound < upper_bound:
    mid = (lower_bound + upper_bound) // 2
    if num_blocks_used(mid,charms) < num_blocks:
        lower_bound = mid
    else:
        upper_bound = mid - 1
print(lower_bound)
assert num_blocks_used(lower_bound, charms) <= num_blocks
assert num_blocks_used(lower_bound + 1, charms) > num_blocks