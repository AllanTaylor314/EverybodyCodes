def to_delta(s):
    d = s[0]
    n = int(s[1:])
    return -n if d == "L" else n


def load_file(part):
    with open(f"everybody_codes_e2025_q01_p{part}.txt") as f:
        lines = f.read().splitlines()
    name_str, _, dir_str = lines
    names = name_str.split(",")
    dirs = dir_str.split(",")
    return names, list(map(to_delta,dirs))


names, dirs = load_file(1)
i = 0
for delta in dirs:
    i += delta
    if i < 0:
        i = 0
    if i >= len(names):
        i = len(names) - 1
print(names[i])

names, dirs = load_file(2)
i = sum(dirs) % len(names)
print(names[i])

names, dirs = load_file(3)
for delta in dirs:
    delta %= len(names)
    names[0], names[delta] = names[delta], names[0]
print(names[0])
