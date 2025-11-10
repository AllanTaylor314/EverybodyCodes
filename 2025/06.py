from collections import Counter


def load_file(part):
    with open(f"everybody_codes_e2025_q06_p{part}.txt") as f:
        lines = f.read().splitlines()
    return lines[0]


line = load_file(1)
num_knights = Counter()
num_pairs = 0
for c in line:
    if c.isupper():
        num_knights[c] += 1
    else:
        if c == "a":
            num_pairs += num_knights["A"]
print(num_pairs)

line = load_file(2)
num_knights = Counter()
num_pairs = 0
for c in line:
    if c.isupper():
        num_knights[c] += 1
    else:
        num_pairs += num_knights[c.upper()]
print(num_pairs)

line = load_file(3)
reps = dist = 1000
# line = 'AABCBABCABCabcabcABCCBAACBCa'
# reps = 1
# dist = 10

looped_pairs = 0
unlooped_pairs = 0
num_knights_loop = Counter(line[:dist]) + Counter(line[-dist:])
num_knights_unloop = Counter(line[:dist])
for i, c in enumerate(line):
    num_knights_loop[line[(i + dist) % len(line)]] += 1
    if i + dist < len(line):
        num_knights_unloop[line[i + dist]] += 1
    if c.islower():
        # print(line[i-dist:i+dist+1])
        # print(c, num_knights_unloop[c.upper()])
        looped_pairs += num_knights_loop[c.upper()]
        unlooped_pairs += num_knights_unloop[c.upper()]
    num_knights_loop[line[(i - dist) % len(line)]] -= 1
    if i - dist >= 0:
        num_knights_unloop[line[i - dist]] -= 1
print(looped_pairs * (reps - 1) + unlooped_pairs)
