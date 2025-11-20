def load_file(part):
    with open(f"everybody_codes_e2025_q13_p{part}.txt") as f:
        lines = f.read().splitlines()
    return [tuple(map(int,line.split('-'))) for line in lines]

def value(ranges,index):
    if index < 0:
        return
    for p in ranges:
        size = p[-1] - p[0] + 1
        if index < size:
            return p[0] + index
        index -= size

def range_size(rng):
    assert rng[0] <= rng[-1]
    return rng[-1] - rng[0] + 1 # inclusive

def solve(part):
    num_iters = int("2025"*part)
    ranges = load_file(part)
    wheel_size = 1 + sum(map(range_size,ranges))
    target_position = num_iters % wheel_size
    return value(ranges[::2],target_position-1) or value(ranges[1::2],wheel_size-target_position-1) or 1

print(*map(solve,(1,2,3)))