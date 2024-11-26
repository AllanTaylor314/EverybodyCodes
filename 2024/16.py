from itertools import zip_longest, count
from operator import mul
from functools import reduce, cache
from collections import Counter
from math import lcm

GOAL = 202420242024

def load_file(part):
    with open(f"everybody_codes_e2024_q16_p{part}.txt") as f:
        header, _, *remainder = f.read().splitlines()
    wheel_distances = list(map(int,header.split(",")))
    wheels_transpose = [[line[i:i+3].strip() for i in range(0,len(line),4)] for line in remainder]
    wheels = [tuple(filter(None,wheel)) for wheel in zip_longest(*wheels_transpose,fillvalue="")]
    return wheel_distances, wheels

def get_line(wheel_positions, wheels):
    return " ".join(wheel[i] for i,wheel in zip(wheel_positions,wheels))

def get_ith_line(i, wheels):
    return " ".join(wheel[i%len(wheel)] for wheel in wheels)

def score_line(line):
    line = line.replace(" ","")
    return sum(i-2 for i in Counter(line).values() if i>2)

wheel_distances, wheels = load_file(1)
wheels = [tuple(wheel[i%len(wheel)] for i,_ in zip(count(step=dist),wheel)) for dist,wheel in zip(wheel_distances,wheels)]
del wheel_distances

print(get_ith_line(100, wheels))

wheel_distances, wheels = load_file(2)
wheels = [tuple(wheel[i%len(wheel)][::2] for i,_ in zip(count(step=dist),wheel)) for dist,wheel in zip(wheel_distances,wheels)]
del wheel_distances

loop_size = lcm(*map(len,wheels))
loop_count, loop_remainder = divmod(GOAL, loop_size)

score_loop = 0
score_rem = 0
for i in range(1,loop_size+1):
    score_loop += score_line(get_ith_line(i,wheels))
    if i == loop_remainder:
        score_rem = score_loop
print(score_loop * loop_count + score_rem)
