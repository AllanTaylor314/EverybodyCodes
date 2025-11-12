from itertools import pairwise


def load_file(part):
    with open(f"everybody_codes_e2025_q08_p{part}.txt") as f:
        return list(map(int,f.read().strip().split(',')))

nums = load_file(1)
total_centre_crossings = 0
for a,b in pairwise(nums):
    if abs(a-b) == 16: # 32//2
        total_centre_crossings+=1
print(total_centre_crossings)

nums = load_file(2)
total_knots = 0
pairs = []
for a,b in pairwise(nums):
    if b < a: a,b=b,a
    pair = a,b
    for c,d in pairs:
        if a < c < b < d or c < a < d < b:
            total_knots += 1
    pairs.append(pair)
print(total_knots)

nums = load_file(3)
pairs = []
for a,b in pairwise(nums):
    if b < a: a,b=b,a
    pair = a,b
    pairs.append(pair)

counts = {}
for a in range(1,257):
    for b in range(a+1,257):
        count = 0
        for c,d in pairs:
            if a < c < b < d or c < a < d < b or (a == c and b == d):
                count += 1
        counts[a,b] = count
print(max(counts.values()))