import re
from math import lcm

def load_file(part):
    with open(f"everybody_codes_e1_q03_p{part}.txt") as f:
        return f.read().splitlines()

def parse_line(line):
    return tuple(map(int, re.match(r"x=(\d+) y=(\d+)",line).groups()))

def snail_score(x, y):
    return x + 100 * y

def step_snail(x, y):
    if y == 1:
        x, y = y, x
    else:
        x += 1
        y -= 1
    return x, y

def is_golden(snails):
    return all(y == 1 for x, y in snails)

def loop_size(x, y):
    return x + y - 1

def days_till_golden(x, y):
    return y - 1

# PART 1
lines = load_file(1)
snails = []
for line in lines:
    x, y = parse_line(line)
    snails.append((x,y))

for _ in range(100):
    snails = [step_snail(x, y) for x, y in snails]

print(sum(snail_score(x,y) for x,y in snails))

# PART 2
lines = load_file(2)
snails = []
for line in lines:
    x, y = parse_line(line)
    snails.append((x,y))

snail_loops = [(loop_size(x,y), days_till_golden(x,y)) for x,y in snails]

# Slow P2
days = 0
while not is_golden(snails):
    snails = [step_snail(x, y) for x, y in snails]
    days += 1
print(days)

# Fast P2
days = 0
total_size = 1
total_offset = 0
for size, offset in snail_loops:
    while (days - offset) % size != 0:
        days += total_size
    total_size = lcm(size, total_size)
print(days)

# PART 3
lines = load_file(3)
snails = []
for line in lines:
    x, y = parse_line(line)
    snails.append((x,y))

snail_loops = [(loop_size(x,y), days_till_golden(x,y)) for x,y in snails]

days = 0
total_size = 1
total_offset = 0
for size, offset in snail_loops:
    while (days - offset) % size != 0:
        days += total_size
    total_size = lcm(size, total_size)
print(days)
