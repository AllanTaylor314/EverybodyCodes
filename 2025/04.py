from math import ceil

def load_file(part):
    with open(f"everybody_codes_e2025_q04_p{part}.txt") as f:
        lines = f.read().splitlines()
    if part == 3:
        return [tuple(map(int,line.split('|'))) for line in lines]
    return [int(line) for line in lines]

sizes = load_file(1)

print(2025 * sizes[0] // sizes[-1] )

sizes = load_file(2)
target = 10000000000000
print(ceil(target * sizes[-1] / sizes[0]))

sizes = load_file(3)
(start,), *mid, (end,) = sizes
alpha = [p[0] for p in mid] + [end]
beta = [start] + [p[1] for p in mid]
ratio = 1
for a,b in zip(alpha,beta):
    ratio *= b/a
print(ratio*100)