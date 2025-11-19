def load_file(part):
    with open(f"everybody_codes_e2025_q13_p{part}.txt") as f:
        lines = f.read().splitlines()
    if part == 1:
        return list(map(int, lines))
    return [tuple(map(int,line.split('-'))) for line in lines]

nums = load_file(1)
dial = [1] + nums[::2] + nums[1::2][::-1]
print(dial[2025%len(dial)])

def value(ranges,index):
    for a,b in ranges:
        size = b - a + 1
        if index < size:
            return a + index
        index -= size

def range_size(rng):
    a,b = rng
    assert a < b
    return b - a + 1 # inclusive

ranges = load_file(2)
wheel_size = 1 + sum(map(range_size,ranges))
target_position = 20252025 % wheel_size
print(value(ranges[::2],target_position-1) or value(ranges[1::2],wheel_size-target_position-1))

ranges = load_file(3)
wheel_size = 1 + sum(map(range_size,ranges))
target_position = 202520252025 % wheel_size
print(value(ranges[::2],target_position-1) or value(ranges[1::2],wheel_size-target_position-1))