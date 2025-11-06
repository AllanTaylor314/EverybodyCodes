from math import ceil


def load_file(part):
    with open(f"everybody_codes_e2025_q04_p{part}.txt") as f:
        lines = f.read().splitlines()
    if part == 3:
        return [tuple(map(int, line.split("|"))) for line in lines]
    return [int(line) for line in lines]


sizes = load_file(1)
print(2025 * sizes[0] // sizes[-1])

sizes = load_file(2)
print(ceil(10000000000000 * sizes[-1] / sizes[0]))

sizes = load_file(3)
(start,), *mid, (end,) = sizes
for a, b in mid:
    start *= b
    end *= a
print(100 * start // end)
