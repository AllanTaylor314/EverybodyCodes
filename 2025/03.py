from collections import Counter

def load_file(part):
    with open(f"everybody_codes_e2025_q03_p{part}.txt") as f:
        line, = f.read().splitlines()
    return list(map(int,line.split(',')))

print(sum(set(load_file(1))))

print(sum(sorted(set(load_file(2)))[:20]))

print(max(Counter(load_file(3)).values()))