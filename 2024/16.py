from itertools import zip_longest, count
from functools import cache
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

wheel_distances, wheels = load_file(3)
wheels = [tuple(w[::2] for w in wheel) for wheel in wheels]


@cache
def maxmin_score(wheel_offset=0,pull_number=0,pulls_remaining=256):
    line = "".join(wheel[(pull_number*dist+wheel_offset)%len(wheel)] for dist,wheel in zip(wheel_distances, wheels))
    score = sum(i-2 for i in Counter(line).values() if i>2) if pull_number else 0
    if pulls_remaining:
        maxs, mins = zip(*(maxmin_score(wheel_offset+i,pull_number+1,pulls_remaining-1) for i in (-1,0,1)))
        return score + max(maxs), score + min(mins)
    return score, score

print(*maxmin_score())
