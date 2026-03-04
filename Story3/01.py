from collections import defaultdict


def load_file(part):
    with open(f"everybody_codes_e3_q01_p{part}.txt") as f:
        return list(map(parse_line, f.read().splitlines()))


def case_bin(s: str):
    return int("".join("1" if c.isupper() else "0" for c in s), 2)


def parse_line(line):
    n, rest = line.split(":")
    rgbs = map(case_bin, rest.split())
    return int(n), *rgbs


data = load_file(1)

print(sum(n for n, r, g, b in data if b < g > r))

data = load_file(2)

print(max(data, key=lambda x: (x[4], -sum(x[1:4])))[0])

data = load_file(3)


def group_of(entry):
    n, r, g, b, s = entry
    is_matte = s <= 30
    is_shiny = s >= 33
    is_red = g < r > b
    is_grn = r < g > b
    is_blu = r < b > g
    shine = "matte" if is_matte else "shiny" if is_shiny else None
    color = "red" if is_red else "green" if is_grn else "blue" if is_blu else None
    if color is None or shine is None:
        return
    return f"{color}-{shine}"


groups = defaultdict(list)
for line in data:
    groups[group_of(line)].append(line[0])
del groups[None]
print(sum(max(groups.values(), key=len)))
